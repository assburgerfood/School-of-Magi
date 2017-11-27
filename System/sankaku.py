#!/usr/bin/python

# sankaku complex (sankakucomplex) image filtering and retrieving/downloading
# script written in Python. You can give scores to every tag you want (in the
# favfile) so the images to fit you the best are the first in the 'winner'
# list.
#
# This file released under public license. Feel free to improve it.
#
# FAVFILE (below) is the path to a taglist with scores in the following format:
# there are 3 symbols: '^' (not), '|' (or) and '&' (and). The not clause can
# only be used at the beginning and negate the whole tags (see De Morgan law).
# Or- and and- clause are used to combine tags together. Using 'or' and 'and'
# leads to an unknown behavior. Here is an example of such file:
#
# tag1 2
# tag2 -5
# tag3|tag1 2
# tag1&tag3 10
# !tag1|tag2 -5
#
# The script print an ordered list of tuples (image id, score) where image id
# is the number you use to access it:
# http://chan.sankakucomplex.com/post/show/<image id>
#
# stdout is strictly used for result in computer/human (JSON) friendly format
# stderr is used for everything else (debug, info and errors)
#
# Enjoy! version 0.1 (2011-01-12)


import http, urllib
from HTMLParser import HTMLParser
from time import sleep
from sys import argv, stderr

# Settings
SITE = "chan.sankakucomplex.com"
REQ = "/post/index.content?%s"
FAVFILE = "tags-fav.txt"
TRESHOLD = 13.0
BOARD_SCORE_CO = 0.30
TRY_LIMIT = 3
DEBUG=False
# Default values
D_TAGS = [ ]
D_PAGES = [ 1 ]
D_SCORE = 0.0

def partition(l, p):
    left = [ ]
    right = [ ]
    for x in l:
        if p(x):
            left.append(x)
        else:
            right.append(x)
    return (left, right)

def partition_key(l, key):
    (a, b) = partition(l, lambda x: x.startswith(key))
    return (a[0][len(key):], b)

def reverse(l):
    a = list(l)
    a.reverse()
    return a

def exists(l, p):
    for x in l:
        if p(x): return True
    return False

def forall(l, p):
    return not exists(l, lambda x: not p(x))

def integer_stream(start=0):
    i = start
    while True:
        yield i
        i += 1

def debug(str):
    if DEBUG:
        print >> stderr, str

def info(str):
    print >> stderr, str

def error(str):
    print >> stderr, str

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list = [ ]
        self.span_id = None
        self.span_open = False
        self.a_src = None

    def handle_starttag(self, tag, attrs):
        if tag == "span":
            value = dict(attrs)
            self.span_id = int(value["id"][1:]) # get image id
            self.span_open = True
        elif tag == "a" and self.span_open:
            value = dict(attrs)
            self.a_src = value["href"]
        elif tag == "img" and self.span_open:
            value = dict(attrs)
            tags = value["title"].split(' ')
            filt = {
                    "id":int(self.span_id),
                    "tags":tags,
                    "src":self.a_src,
                    }
            for key in [ "user", "rating", "score" ]:
                filt[key] = partition_key(tags, key+":")[0]
            filt["score"] = float(filt["score"])
            self.list.append( filt )

    def handle_endtag(self, tag):
        if tag == "span":
            self.span_id = None
            self.span_open = False


# List of images with dict entries (id, tags, score, src, user, rating)
def get_page(tags_list, page):
    info("Getting page %i" % (page))
    params = urllib.urlencode({ "tags":' '.join(tags_list), "page":page })
    url = REQ % (params)
    c = httplib.HTTPConnection(SITE)
    counter = 0
    while True:
        c.request("GET", url, "", { "Accept": "text/html" })
        r = c.getresponse()

        if r.status == 500 and counter < TRY_LIMIT:
            error("Page %i error 500, trying again!" % (page))
            sleep(0.5) # trying again
            counter += 1
            continue
        if r.status == 404:
            error("Page %i error 404, returns empty" % (page))
            return [ ]
        if r.status != 200:
            raise Exception("Page %s status error %i" % (page, r.status))
            return [ ]

        p = Parser()
        data = r.read()
        p.feed(data)
        return p.list

# List of (tag, score) from the file
def get_favs(file):
    favs = [ ]
    try:
        with open(file, "r") as f:
            for line in f:
                try:
                    (tag, score) = line.split()
                except:
                    raise Exception("Error in fav file: %s" % (line))
                favs.append( (tag, float(score)) )
    except:
        error("You have to create a taglist file, see in the .py")
        exit()
    return favs

def get_img_score(img, tags_scores):
    debug("computing image score: %s" % (img))
    tot = D_SCORE
    # use user tags scores
    for (tag, score) in tags_scores:
        if tag[0] == "^": # 'not' clause (with '^' at begining)
            tag = tag[1:]
            debug("not-tag %s score %i+(%i)" % (tag, tot, score))
            tot += score
            score *= -1
        if "|" in tag: # 'or' clause (using | as separator)
            or_tags = tag.split("|")
            if exists(or_tags, lambda x: x in img["tags"]):
                debug("or-tags %s +%i" % (or_tags, score))
                tot += score
        elif "&" in tag: # 'and' clause (using & as separator)
            and_tags = tag.split("&")
            if forall(and_tags, lambda x: x in img["tags"]):
                debug("and-tags %s +%i" % (and_tags, score))
                tot += score
        elif tag in img["tags"]:
            debug("tag %s +%i" % (tag, score))
            tot += score
    # add bonus for board scores
    board_extra = img["score"] * BOARD_SCORE_CO
    debug("bonus board score +%f (%i)" % (board_extra, img["score"]))
    tot += board_extra
    debug("score total: %i" % (tot))
    return tot

def help():
    error("%s usage:" % (argv[0]))
    error("\t-t: takes tags, comma separated.")
    error("\t\te.g.: -ttag1,tag2")
    error("\t-p: takes pages, comma separated or 'all'")
    error("\t\te.g.: -p4,5,6 or -pall")

if __name__ == "__main__":
    imgs = [ ]
    tags = D_TAGS
    pages = D_PAGES

    if len(argv) >= 0 and ("help" in argv or "-h" in argv):
        help()
        exit()
    else:
        for opt in argv[1:]:
            if opt.startswith("-t"): # tags
                tags = opt[2:].split(",")
            elif opt.startswith("-p"): # pages
                arg = opt[2:]
                if arg.startswith("all"):
                    start = 1
                    all_arg = arg[3:]
                    if all_arg.startswith(":"):
                        start = int(all_arg[1:])
                    pages = integer_stream(start)
                    info("Fetching pages until user asks us to stop, " \
                            "press Ctrl+C to stop!")
                else:
                    pages = map(lambda x: int(x), arg.split(","))

    # print options
    debug("pages: %s, tags: %s" % (pages, tags))

    user_tags = get_favs(FAVFILE)
    for page in pages:
        try:
            l = get_page(tags, page)
        except KeyboardInterrupt:
            info("User interruption, stop fetching")
            break
        if len(l) == 0:
            info("List empty, stopping for now")
            break
        imgs += l
    imgs_score = map(lambda x: (x, get_img_score(x, user_tags)), imgs)
    imgs_best = reverse(sorted(filter(lambda (i,s): s >= TRESHOLD, \
            imgs_score), key=lambda (i,s): s))

    debug("List: %s" % imgs)
    debug("Scores: %s" % imgs_score)
    info("Winners:")
    print map(lambda (i,s): (i["id"], s), imgs_best)
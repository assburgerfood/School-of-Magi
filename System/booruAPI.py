import random
import urllib.request

from pybooru import Danbooru
from pybooru import Moebooru


class DanGET:
    def __init__(self, _tags):
        client = Danbooru('danbooru')
        self.posts = client.post_list(limit=1, tags=_tags)

    def picture(self):
        for post in self.posts:
            return post['file_url']


class MoeGET:
    def __init__(self, _tags, _pages, _booru):
        r = random.randint(1, 40 * _pages)
        client = Moebooru(_booru)
        print(_tags, _pages)
        self.posts = client.post_list(limit=1, tags=_tags, page=r)

    def picture(self):
        url = self.posts[0]['file_url']
        print("Yande URL: ", url)
        return urllib.request.urlopen(url).read()


if __name__ == '__main__':
    yan = MoeGET("ai", 10, 'yandere').picture()
    print(yan)

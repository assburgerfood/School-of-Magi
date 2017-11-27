import random
import urllib.request

import pybooru
from PyQt5.QtGui import QImage, QPixmap
from pybooru import Danbooru
from pybooru import Moebooru


class DanGET(pybooru.danbooru.Danbooru):
    def __init__(self, _tags):
        client = Danbooru('danbooru')
        self.posts = client.post_list(limit=1, tags=_tags)

    def picture(self):
        for post in self.posts:
            return post['file_url']


class YanGET(pybooru.moebooru.Moebooru):
    def __init__(self, _tags, _pages):
        r = random.randint(1, 40 * _pages)
        client = Moebooru('yandere')
        self.posts = client.post_list(limit=1, tags=_tags, page=r)

    def picture(self):
        url = self.posts[0]['file_url']
        print("Yande URL: ", url)
        data = urllib.request.urlopen(url).read()
        image = QImage()
        image.loadFromData(data)
        return QPixmap(image)

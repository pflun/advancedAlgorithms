# -*- coding: utf-8 -*-
# https://www.1point3acres.com/bbs/interview/dropbox-software-engineer-327178.html
# NASA selects Dropbox as its official partner, and we’re tasked with managing
# a panorama for the universe. The Hubble telescope (or some other voyager we
# have out there) will occasionally snap a photo of a sector of the universe,
# and transmit it to us. You are to help write a data structure to manage this.
# For the purpose of this problem, assume that the observable universe has been
# divided into 2D sectors. Sectors are indexed by x- and y-coordinates.

class File(object):
    def __init__(self, path, exists):
        self.path = path # str
        self.exists = exists # bool

    def read(self):
        file = ""
        return file

    def write(self):
        return

class Image(object):
    def __init__(self, image):
        self.image = image

    def getBytes(self):
        return

class Sector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class SpacePanorama(object):
    def __init__(self, rows, cols):
        self.matrix = [[None for _ in range(cols)] for _ in range(rows)]

    def update(self, y, x, image):
        return

    def fetch(self, y, x):
        return

    # LRU Cache
    def getStalestSector(self):
        return
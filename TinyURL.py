import hashlib
import time
print type(time.time())

a = "http://site.douban.com/chuan"
# 32 byte
print hashlib.md5(a).hexdigest()
class TinyURL:
    def __init__(self):
        self.url_pair = {}

    def encode(self, longUrl):
        hashed = hashlib.md5(longUrl).hexdigest()
        if hashed[:6] in self.url_pair:
            hashed = hashlib.md5(longUrl + str(time.time())).hexdigest()
        self.url_pair[hashed[:6]] = longUrl

        return 'http://tinyurl.com/' + hashed[:6]


    def decode(self, shortUrl):
        if shortUrl[19:] in self.url_pair:
            return self.url_pair[shortUrl[19:]]
        else:
            return 'Not found'



codec = TinyURL()
url = 'http://tinyurl.com/123456'
print codec.encode(url)
print codec.decode(codec.encode(url))
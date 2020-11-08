# https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md
class Page(object):
    def __init__(self, url, contents, child_urls):
        self.url = url
        self.contents = contents
        self.child_urls = child_urls

class Crawler(object):
    def __init__(self):
        self.queue = []
        self.visited = set()
        self.dic = {} # url => text

    def crawl(self):
        while self.queue:
            currUrl = self.queue.pop(0)
            if currUrl in self.visited:
                continue
            self.crawlPage(currUrl)

    def crawlPage(self, url):
        self.visited.add(url)
        # visit url to get Page
        page = self.getPage(url)
        for link in page.child_urls:
            self.queue.append(link)
        if url not in self.dic:
            self.dic[url] = page.contents

    def getPage(self, url):
        # assume return web page
        return Page(url, '', [])
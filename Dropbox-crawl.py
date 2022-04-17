# -*- coding: utf-8 -*-
# https://leetcode.com/problems/web-crawler-multithreaded/discuss/417762/Python3-Thread-%2B-Lock-implementation%3A-256-ms.-ThreadPool%3A-300-ms.
from threading import Thread
from threading import Lock
import collections

class Solution:
    def __init__(self):
        self.queue = []
        self.visited = set()
        self.lock = Lock()

    def getHostName(self, url):
        return url.split('/')[2]

    # worker
    def worker(self, curr_url, htmlParser):
        next_urls = htmlParser.getUrls(curr_url)

        # Acquire lock to ensure urls are no en-queued multiple times
        # with self.lock 和acquire再release一样
        for url in next_urls:
            if url not in self.visited and self.curr_hostname == self.getHostName(url):
                self.lock.acquire()
                self.queue.append(url)
                self.visited.add(url)
                self.lock.release()

    def crawl(self, startUrl, htmlParser):
        self.queue.append(startUrl)
        # crawl all links that are under the same hostname
        self.curr_hostname = self.getHostName(startUrl)
        self.visited.add(startUrl)

        while self.queue:
            threads = []
            # If there are still URLs in the queue, add to the thread list
            while self.queue:
                curr_url = self.queue.pop(0)
                threads.append(Thread(target=self.worker, args=(curr_url, htmlParser)))

            # Execute this batch of threads
            for thread in threads:
                thread.start()

            # Main thread waiting for the above threads to finish
            # join的原理就是依次检验线程池中的线程是否结束，没有结束就阻塞直到线程结束
            # 没有下面join检查就会提前结束了，因为不wait先执行完就不管其他thread先返回了，同理join(2)就代表每个/这个thread只等2秒，超过2秒就不等了
            for thread in threads:
                thread.join()

        return list(self.visited)

    def crawlSingleThread(self, startUrl, htmlParser):
        self.queue.append(startUrl)
        self.curr_hostname = self.getHostName(startUrl)
        self.visited.add(startUrl)

        while self.queue:
            curr_url = self.queue.pop(0)
            next_urls = htmlParser.getUrls(curr_url)
            for url in next_urls:
                if url not in self.visited and self.curr_hostname == self.getHostName(url):
                    self.queue.append(url)
                    self.visited.add(url)
        return list(self.visited)

    def crawlDFS(self, startUrl, htmlParser):
        def worker(url, htmlParser):
            urls = htmlParser.getUrls(url)
            dfs(urls, htmlParser)

        def dfs(urls, htmlParser):
            threads = []
            for url in urls:
                if url not in self.visited and self.curr_hostname == self.getHostName(url):
                    self.visited.add(url)
                    x = Thread(target=worker, args=(url, htmlParser))
                    x.start()
                    threads.append(x)
            for thread in threads:
                thread.join()

        self.curr_hostname = self.getHostName(startUrl)
        dfs([startUrl], htmlParser)
        return list(self.visited)

test = Solution()
print test.getHostName("http://www.leetcode.com/contest")
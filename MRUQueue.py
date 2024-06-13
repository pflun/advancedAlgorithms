class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.queue = [i for i in range(1, n + 1)]

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        res = self.queue[k - 1]
        self.queue = self.queue[:k - 1] + self.queue[k:] + [res]
        return res
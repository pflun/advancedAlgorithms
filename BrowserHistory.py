class LinkedNode(object):
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class BrowserHistory(object):

    def __init__(self, homepage):
        self.curr = LinkedNode(homepage)

    def visit(self, url):
        newNode = LinkedNode(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode

    def back(self, steps):
        while steps > 0:
            if not self.curr.prev:
                return self.curr.value
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.value

    def forward(self, steps):
        while steps > 0:
            if not self.curr.next:
                return self.curr.value
            self.curr = self.curr.next
            steps -= 1
        return self.curr.value

browserHistory = BrowserHistory("leetcode.com")
print browserHistory.visit("google.com")
print browserHistory.visit("facebook.com")
print browserHistory.visit("youtube.com")
print browserHistory.back(1)
print browserHistory.back(1)
print browserHistory.forward(1)
print browserHistory.visit("linkedin.com")
print browserHistory.forward(2)
print browserHistory.back(2)
print browserHistory.back(7)
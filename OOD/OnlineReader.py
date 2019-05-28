class Library(object):
    def __init__(self):
        self.books = []

    def addBook(self):
        pass

    def removeBook(self):
        pass

class Book(object):
    def __init__(self):
        self.bid = 0
        self.content = ''

    def getContent(self):
        pass

class UserManager(object):
    def __init__(self):
        self.users = []

    def addUser(self, uid, username):
        pass

    def removeUser(self, uid):
        pass

class User(object):
    def __init__(self):
        self.uid = 0
        self.username = ''
        self.membership = False

    def renewMembership(self):
        pass

class Display(object):
    def __init__(self):
        self.currBook = 0
        self.currUser = 0
        self.currpage = 0

    def show(self, bid, currpage):
        pass

    def nextPage(self):
        self.currpage += 1

    def prevPage(self):
        self.currpage -= 1
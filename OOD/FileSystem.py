class Entry(object):
    def __init__(self):
        self.name = ''
        self.parent = ''
        self.created = 0
        self.lastUpdate = 0
        self.lastAccess = 0

    def create(self):
        pass

    def delete(self):
        pass

    def getFullPath(self):
        if not self.parent:
            return self.name
        else:
            return self.parent + '/' + self.name

    # get created time, last update time, change name etc

class Directory(Entry):
    def __init__(self):
        super(Directory, self).__init__()
        self.content = []

    def numberOfFiles(self):
        pass

    def getSize(self):
        pass

class File(Entry):
    def __init__(self):
        super(File, self).__init__()
        self.content = ''
        self.size = 0

    def getContent(self):
        pass

    def setContent(self):
        pass

    def getSize(self):
        pass

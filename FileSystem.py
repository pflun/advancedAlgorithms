# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]
#
# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/"); // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/"); // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

class TrieNode(object):
    def __init__(self):
        self.name = None
        self.children = {}
        self.isFile = False
        self.content = []

class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path):
        node = self.search(path)
        if not node:
            return []
        if node.isFile:
            return [node.name]
        return list(node.children.keys())

    def mkdir(self, path):
        self.insert(path, False)

    def addContentToFile(self, filePath, content):
        node = self.insert(filePath, True)
        node.content.append(content)
        return

    def readContentFromFile(self, filePath):
        node = self.search(filePath)
        return ''.join(node.children)

    # helper
    def insert(self, path, isFile):
        node = self.root
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
        node.isFile = isFile
        if isFile:
            node.name = ps[-1]
        return node

    def search(self, path):
        node = self.root
        if path == '/':
            return node
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                return None
            node = node.children[p]
        return node
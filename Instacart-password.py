class Solution(object):
    def read1(self, fname):
        with open(fname) as f:
            texts = f.read().splitlines()
        f.close()
        return texts

    def getChar1(self):
        chunk = self.read1('Instacart-password1.txt')
        pos = chunk[0].strip('][').split(', ')
        y = int(pos[1])
        x = int(pos[0])
        return chunk[-y - 1][x]

    def read(self, fname):
        with open(fname) as f:
            texts = f.read().splitlines()
        f.close()

        parsed_texts = []
        tmp = []
        for t in texts:
            if t == "":
                parsed_texts.append(tmp)
                tmp = []
            else:
                tmp.append(t)
        parsed_texts.append(tmp)
        return parsed_texts

    def getChar(self, chunk):
        pos = chunk[1].strip('][').split(', ')
        y = int(pos[1])
        x = int(pos[0])
        return chunk[-y - 1][x]

    def getPassword(self):
        parsed_texts = self.read('Instacart-password2.txt')
        res = [None for _ in range(len(parsed_texts))]
        for t in parsed_texts:
            char = self.getChar(t)
            idx = int(t[0])
            res[idx] = char
        return ''.join(res)

    def getFirstPassword(self):
        parsed_texts = self.readFirstPassword('Instacart-password3.txt')
        res = [None for _ in range(len(parsed_texts))]
        for t in parsed_texts:
            char = self.getChar(t)
            idx = int(t[0])
            res[idx] = char
        return ''.join(res)

    def readFirstPassword(self, fname):
        idxes = set()
        res, tmp = [], []
        f = open(fname, "r")
        curr = f.readline().rstrip('\n')
        while True:
            if curr.isdigit() and curr in idxes:
                break
            if curr.isdigit():
                idxes.add(curr)
            if curr == "":
                res.append(tmp)
                tmp = []
            else:
                tmp.append(curr)
            curr = f.readline().rstrip('\n')
        return res

test = Solution()
print test.getChar1()
print test.getPassword()
print test.getFirstPassword()
print test.readFirstPassword("Instacart-password3.txt")
print test.read("Instacart-password3.txt")

# while True:
#     line = file1.readline()
#     if not line:
#         break

print '[2, 3]'.strip('[]')
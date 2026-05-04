class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        self.dic = {}
        self.freq = {}
        for i in range(len(keys)):
            self.dic[keys[i]] = values[i]
        for w in dictionary:
            encrypt_w = self.encrypt(w)
            self.freq[encrypt_w] = self.freq.get(encrypt_w, 0) + 1

    def encrypt(self, word1):
        res = ''
        for w in word1:
            if w not in self.dic:
                return ''
            res += self.dic[w]
        return res

    def decrypt(self, word2):
        return self.freq.get(word2, 0)

test = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
print test.encrypt("abcd")
print test.decrypt("eizfeiam")
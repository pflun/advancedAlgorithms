class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for w in words:
            tmp = ""
            for c in w:
                tmp += morse[ord(c) - 97]
            res.add(tmp)
        return len(res)
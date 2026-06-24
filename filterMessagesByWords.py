# Return only the safe messages, meaning those whose text contains no unsafe word, preserving the original order.
# Word matching follows two rules:
# A word is a maximal sequence of characters delimited by spaces: punctuation is part of the word, not a separator, so "Nintendo," and "Nintendo" are distinct words.
# Matching is case-insensitive: "nintendo" and "NINTENDO" are the same word.
# Input: messages = [["tom", "i am enjoying the nintendo switch"], ["jerry", "i prefer the wii"], ["tom", "my best friend is sonya"], ["tom", "do you have a usb charger"], ["jerry", "no but i do have a USB-C charger"], ["dan", "dafNintendo-doo is a fun app"]], unsafeWords = ["Nintendo", "Microsoft", "SONY", "usb-C"]
# Output: [["jerry", "i prefer the wii"], ["tom", "my best friend is sonya"], ["tom", "do you have a usb charger"], ["dan", "dafNintendo-doo is a fun app"]]
class Solution:
    def filterMessagesByWords(self, messages, unsafeWords):
        res = []
        unsafeSet = set()
        for w in unsafeWords:
            unsafeSet.add(w.lower())
        for m in messages:
            safe = True
            words = m[1].split(' ')
            for w in words:
                if w.lower() in unsafeSet:
                    safe = False
                    break
            if safe:
                res.append(m)
        return res

test = Solution()
print test.filterMessagesByWords([["tom", "i am enjoying the nintendo switch"], ["jerry", "i prefer the wii"],
                                  ["tom", "my best friend is sonya"], ["tom", "do you have a usb charger"],
                                  ["jerry", "no but i do have a USB-C charger"], ["dan", "dafNintendo-doo is a fun app"]],
                                 ["Nintendo", "Microsoft", "SONY", "usb-C"])
print test.filterMessagesByWords([["a", "Nintendo is great"], ["b", "I love my NintendoSwitch"], ["c", "SONY sells TVs"],
                                  ["d", "sonya is my friend"], ["e", "Buy usb-c today"], ["f", "I use USB cable"]],
                                 ["Nintendo", "SONY", "usb-C"])
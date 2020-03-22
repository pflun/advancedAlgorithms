class Solution(object):
    def deckRevealedIncreasing(self, deck):
        cards = [i for i in range(len(deck))]
        idxs = []
        while cards:
            first = cards[0]
            idxs.append(first)
            cards = cards[1:]
            if len(cards) > 1:
                cards = cards[1:] + [cards[0]]
        res = [0 for _ in range(len(deck))]
        deck.sort()
        deck = iter(deck)
        for i in idxs:
            card = deck.next()
            res[i] = card
        return res

test = Solution()
print test.deckRevealedIncreasing([17,13,11,2,3,5,7])
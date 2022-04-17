def getFactorFromCard(card, idx):
    # suit
    if idx == 0:
        return card[0]
    # value
    elif idx == 1:
        return card[1]
    # count
    else:
        return len(card) -1

def isMeetCondition(c1, c2, c3, idx):
    m1 = getFactorFromCard(c1, idx)
    m2 = getFactorFromCard(c2, idx)
    m3 = getFactorFromCard(c3, idx)
    return m1 == m2 == m3 or m1 != m2 != m3 != m1

def findValidHand(cards):
    n = len(cards)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                boolean = True
                for l in range(3):
                    if not isMeetCondition(cards[i], cards[j], cards[k], l):
                        boolean = False
                        break
                if boolean:
                    return [cards[i], cards[j], cards[k]]
    return 0

# only return first found
print findValidHand(["-A", "-B", "-BB", "+C", "-C", "=CCC"])
print findValidHand(["-A", "-A", "-A", "+CC", "-C", "=CCC"])
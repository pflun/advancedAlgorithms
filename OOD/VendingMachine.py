class VendingMachine(object):
    def __init__(self):
        # Coke => 10 left
        self.itemInventory = {}
        # Coke => 1.99
        self.price = {}
        self.currentItem = ''
        self.currentBalance = 0

    def selectItemAndGetPrice(self, item):
        if self.itemInventory[item] > 0:
            self.currentItem = item
            return self.price[item]
        else:
            print 'Out of stock'

    def insertCoin(self, coin):
        self.currentBalance += coin

    def checkout(self):
        if self.isFullPaid():
            self.currentBalance -= self.price[self.currentItem]
            self.itemInventory[self.currentItem] -= 1
        else:
            print 'not enough coins'

        checkoutItem = self.currentItem
        self.currentItem = ''
        return checkoutItem

    def isFullPaid(self):
        if self.currentBalance >= self.price[self.currentItem]:
            return True
        else:
            return False

    def refund(self):
        refund = self.currentBalance
        self.currentBalance = 0
        return refund
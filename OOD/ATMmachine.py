class Bank(object):
    def __init__(self, bankName):
        self.bankName = bankName
        # Map of ID => bank account
        self.accounts = {}
        # List of atms
        self.atms = []

class bankAccount(object):
    def __init__(self, accountID, initialBalance):
        self.id = accountID
        self.balance = initialBalance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class ATM(object):
    def __init__(self, name):
        self.atmName = name

    def getAccount(self, bank, accountID):
        if accountID in bank.accounts:
            return bank.accounts[accountID]

    def processTransaction(self, account, action, amount):
        if action == 'exit':
            return
        elif action == 'deposit':
            account.deposit(amount)
        elif action == 'withdraw':
            account.withdraw(amount)
        elif action == 'balance':
            return account.balance
        else:
            return 'Unknown acton'

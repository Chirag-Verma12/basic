class Bank:
    def __init__(self, name, account_no,  bank_no, bank_balance, address):
        self.name = name
        self.account_no = account_no
        self.bank_no = bank_no
        self.__bank_balance = bank_balance 
        self.address = address
        if(self.name == "Chirag") or (self.name == "chirag"):
            print(self.name)
        else:
            exit()
        
    def withdraw(self, pin, amount):
        self._pin = pin 
        if(self._pin != 2012):
            print("\ninvalid")
            exit()
        self.__bank_balance -= amount
        print("\nRs.", amount, "has been withdrawed")
        print("current balance =", self.showbalance())
        

    def credit(self, amount):
        self.__bank_balance += amount
        print("\nRs.", amount, "has been credited")
        print("\ncurrent balance:", self.showbalance())

    def showbalance(self):
        return self.__bank_balance

s1 = Bank("asd", 22334455, 445566, 44556677, "b-255")
print(s1.address)

s1.withdraw(2012, 2312)


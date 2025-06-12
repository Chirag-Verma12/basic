class Bank:
    def __init__(self, name, account_no, bank_balance, address):
        self.name = name
        self.account_no = account_no
        self.__bank_balance = bank_balance 
        self.address = address

    def withdraw(self, pin, amount):
        self._pin = pin 
        if(self._pin != 2012):
            print("\nInvalid PIN Entered")
            exit()

        if(amount > self.__bank_balance):
            print("\nInsufficient Balance")

        else:
            self.__bank_balance -= amount
            print("\nRs.", amount, "has been withdrawed")
            print("current balance =", self.showbalance())
        

    def credit(self, amount):
        self.__bank_balance += amount
        print("\nRs.", amount, "has been credited")
        print("current balance:", self.showbalance())
  
    def showbalance(self):
        return self.__bank_balance
    
    
user = input("Enter your Name:\t")
if(user.lower() == "chirag"):
    print("\n**************\n   Accessed\n**************\n")

else:
    print("Declined")

s1 = Bank("Chirag", 223344, 4000, "b-255")

bank_user = Bank(name="chirag", account_no=223344, bank_balance=10000, address="b-255")
while True:
    print("\n----Bank Menu----")
    print("1. withdraw money")
    print("2. credit money")
    print("3. show balance")
    print("4. exit")

    choice = input("Enter your choice btw (1 - 4):\t")
    if(choice == "1"):
        pin = int(input("Enter your PIN:\t"))
        amount = float(input("Enter the amount you want to withdraw:\t"))
        bank_user.withdraw(pin, amount)

    elif(choice =="2"):
        amount = float(input("Enter the amount you want to add:\t"))
        bank_user.credit(amount)
    
    elif(choice == "3"):
        print("Your current balance:\t", bank_user.showbalance())
    
    elif(choice == "4"):
        print("Exicting..... Thank's for visiting..")
        break
    else:
        print("Invalid choice... choose btw 1 - 4 pls..")

    leave = input("\nNow do you want to leave:\t")
    if(leave.lower() == "yes"):
        break


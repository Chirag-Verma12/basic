import os

class Bank:
    def __init__(self, name, account_no, bank_balance, address, pin):
        self.name = name
        self.account_no = account_no
        self.__bank_balance = bank_balance 
        self.address = address
        self.__pin = pin 

    def authenticator(self, entered_pin):
          return self.__pin == entered_pin
            

    def withdraw(self, amount):
        if(amount > self.__bank_balance):
            return "\nInsufficient Balance"
        self.__bank_balance -= amount
        self.__log_transaction(f"Withdraw Rs. {amount}")
        return f"Rs.{amount} has been withdrawed.\nCurrent balance {self.__bank_balance}"
        
    def credit(self, amount):
        self.__bank_balance += amount
        self.__log_transaction (f"credited Rs. {amount}")
        return f"Rs. {amount} has been credited.\nCurrent balance {self.__bank_balance}"
  
    def showbalance(self):
        return self.__bank_balance
    
    def __log_transaction(self, message):
        with open(f"{self.name}_transaction.txt", "a") as file:
            file.write(f"{message}\n")

class banksystem:
    def __init__(self):
        self.user == {}
    
    def add_user(self, bank_user):
        self.users[bank_user.name.lower()] = bank_user
    
    def run(self):
        user_name = input("Enter your Name:\t").lower()
        if user_name not in self.users:
            print("Access Denied: user not found.")
            return
        
        bank_user = self.users[user_name]
        try:
            pin = int(input("Enter your 4-digit PIN:\t"))
        except ValueError:
            print("invalid PIN formate")
            return
        if not bank_user.authenticate(pin):
            print("Incorrect PIN. access deined.")
            return

    print("\n**************\n   Accessed\n**************\n")


#bank_user = Bank(name="chirag", account_no=223344, bank_balance=10000, address="b-255")
while True:
    print("\n----Bank Menu----")
    print("1. withdraw money")
    print("2. credit money")
    print("3. show balance")
    print("4. exit")

    choice = input("Enter your choice btw (1 - 4):\t").strip()
    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount")

    elif(choice =="2"):
        try:
            amount = float(input("Enter amount to credit: "))
            print(bank_user.credit(amount))
        
        except ValueError:
            print("Invalid amount")
    
    elif(choice == "3"):
        print("Your current balance:\t", bank_user.showbalance())
    
    elif(choice == "4"):
        print("Exicting..... Thank's for visiting..")
        break
    else:
        print("Invalid choice... choose btw 1 - 4 pls..")

    leave = input("\nNow do you want to leave:\t").strip().lower()
    if(leave.lower() == "yes"):
        break

system = banksystem()
user1 = Bank(name="Chirag", account_no=223344, bank_balance=10000, address="b-255", pin=2012)
system.add_user(user1)

system.run()
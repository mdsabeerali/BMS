                                                     #BANKING MANAGEMENT SYSTEM



import random 

class Bank:
    '''This class is used to create a bank object with some functions.'''

    def __init__(self):
        self.amount = 0
        self.account_no = random.randint(128030,999999)
        self.name = input("Enter the name: ")
        self.bank_name = input("Enter your bankname: ")

    def Withdraw(self):
        '''This method is used to withdraw the money from the bank'''

        self.money_withdraw = int(input("Enter the money to withdraw"))
        
        if(self.money_withdraw<self.amount):
            self.amount = self.amount - self.money_withdraw
            print("You have successfully withdrawn the money.")
        else:
            print("You don't have sufficient balance.")
            print(f"your Balance = {self.amount} ")
        self.amount = self.amount - self.money_withdraw
        self.Display_Balance()

    def Deposit(self):
        '''This method is used to deposit the money in the bank'''

        self.money_deposit = int(input("Enter the amount of money u want to deposit:"))
        self.amount = self.amount + self.money_deposit
        self.Display_Balance()

    def Display(self):
        '''This method is used to display the information of the user'''

        print("----INFO---")
        print(f"Name = {self.name}")
        print(f'accout_no = {self.account_no}')
        print(f'Bank_name = {self.bank_name}')
        print(f'Balance = {self.amount}')
    
    def Display_Balance(self):
        '''This method is used to display the balance'''

        print(f"Balance = {self.amount}")

    def update(self):
        '''This method is used to update the details of the user'''
          
        New_name = input(f"Enter your new name or if you want default then leave blank :")
        if New_name!="":
            self.name = New_name
        New_bank_name = input(f"Enter your new bank_name or if you want default then leave blank :")
        if New_bank_name!="":
            self.bank_namename = New_bank_name

accounts = []
def Search_accno(account_number):
    for i in accounts:
        if i.account_no == account_number:
            return i
    else:
        return None
        
while True:
    print("1. Add a account")
    print("2. Print all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Transfer")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print(f'You have successfully added the account and your account no is {obj.account_no}')
    elif choice == 2:
        if len(accounts)==0:
            print("No accounts found!")
        else:
            for i in accounts:
                i.Display()

    elif choice == 3:
        acc_no = int(input("Enter the accout no: "))
        for i in accounts:
            if i.account_no == acc_no:
                print(i.Display())
                break
        else:
            print("Your account doesn't exist.")


    elif choice == 4:
        acc_no = int(input("Enter the account no: "))
        for i in accounts:
            if i.account_no == acc_no:
                i.Deposit()
                break
        else:
            print("Your account doesn't exist.")
            

    elif choice == 5:
        acc_no = int(input("Enter the account no: "))
        for i in accounts:
            if i.account_no == acc_no:
                i.Withdraw()
                break
        else:
            print("Your account doesn't exist.")
    
    elif choice == 6:
        acc_no = int(input("Enter the account no: "))
        result = Search_accno(acc_no)
        if result!= None:
            result.Display_Balance()

    elif choice == 7:
        acc_no = int(input("Enter your account number: "))
        Sender_acc = Search_accno(acc_no)
        if(Sender_acc!=None):
            rec_acc_no = int(input("Enter the account no which u want to transfer: "))
            receiver_acc = Search_accno(rec_acc_no)
            if receiver_acc != None:
                transfer_amount = int(input("Enter the money you want to send: "))
                if transfer_amount<Sender_acc.amount:
                    Sender_acc.amount -= transfer_amount
                    receiver_acc.amount += transfer_amount
                    print(f'You have successfully transferred the money and Balance = {Sender_acc.amount}')
                else:
                    print(f"You don't have enough money Balance = {Sender_acc.amount}")
            else:
                print("Receiver account_no is invalid.")
        else:
            print("Your account doesn't exist.")

    elif choice == 8:
        break
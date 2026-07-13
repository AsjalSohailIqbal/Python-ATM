def show_menu():
    print('''
        Select Input:
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Transfer
        5. Change PIN
        6. History
        7. Exit
        ''')

def check_balance(balance):
    print("Balance:",balance,sep="")
    
def deposit(balance,history):
    while True:
        amount_deposit=int(input("Enter Amount:"))
        if amount_deposit>0:
            balance+=amount_deposit
            print('New Balance:',balance,sep="")
            history.append(f"Deposited {amount_deposit}")
            return balance
        else:
            print("Invalid Amount")

def withdraw(balance,history):
    while True:
        amount_withdraw=int(input("Enter Amount:"))
        if amount_withdraw<=0:
            print("Invalid Amount")
        elif amount_withdraw>balance:
            print("Insufficient Balance, Existing Balance:",balance,sep="")
        else:
            balance-=amount_withdraw
            print("New Balance:",balance,sep="")
            history.append(f"Withdrawn {amount_withdraw}")
            return balance

def transfer(balance,history):
    while True:
        receiver_name=input("Enter Receiver Name:")
        amount_transfer=int(input("Enter Amount:"))
        if amount_transfer<=0:
            print("Invalid Amount")
        elif amount_transfer>balance:
            print("Insufficient Balance, Existing Balance:",balance,sep="")
        else:
            balance-=amount_transfer
            print("Transferred",amount_transfer,"to",receiver_name)
            history.append(f"Transferred {amount_transfer} to {receiver_name}")
            return balance

def change_pin(current_pin,history):
    while True:
        old_pin = input("Enter current PIN:")
        if old_pin != current_pin:
            print("Pin doesn't match")
        else:    
            while True:    
                new_pin = input("Enter new PIN:")
                if new_pin.isdigit():
                    if len(new_pin) != 4:
                        print("Invalid Input, Enter a four digit PIN")
                        continue
                    elif new_pin == old_pin:
                        print("New PIN cannot be same as Old PIN")
                    else:
                        print("PIN changed successfully")
                        history.append("PIN Changed")
                        return new_pin
                else:
                    print("Invalid Input, Enter a four Digit Pin")

def show_history(history):
    if len(history)>0:
        for transaction in history:
            print(transaction)
            print()
    else:
        print("No Transactions Yet")
    
def atm(current_pin):
    balance=5000
    history=[]
    
    while True:
    
        show_menu()   
    
        choice=int(input('Enter Choice:'))

        match choice:

            case 1:
                check_balance(balance)

            case 2:
                balance=deposit(balance,history)

            case 3:
                balance=withdraw(balance,history)
   
            case 4:
                balance=transfer(balance,history)
    
            case 5:
                current_pin=change_pin(current_pin,history)

            case 6:
                show_history(history)
   
            case 7:
                print('Thank you for using our ATM')
                return current_pin
    
            case _:
                print("Invalid Input, Try Again")
                
print("Welcome to ATM")

old_pin = '1234'
attempts=3

while attempts>0:
    pin=input("Enter Pin:")
    if pin == old_pin:
        old_pin = atm(old_pin)
        break
    
    elif attempts>1:
        attempts-=1
        print("Wrong Attempt, Attempts Left:",attempts)
    else:
        print("Account Locked")
        break

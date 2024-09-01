#create account
accounts={}
def create_account(account_holder ,account_number,initial_balance):
    if create_account in accounts:
            return "account already exits"
    elif account_balance>0:
            return "initial balance must be non-negative or greater then zero"
    accounts[account_number]={
           "account_holder/user": account_holder,
           "balance": initial_balance
    }
    return"account created succesfully"
#deposit money
def deposit_money(account_number,amount):
    if account_number not in accounts:
              return"account not found"
    if amount<=0:
           return"amount be positive"
    accounts[account_number][balance]+=amount
    return f"deosited{amount}successfully.new balance:{accounts[account_number][balance]}"
#withdraw money
def withdraw_money(account_number,amount):
    if account_number not in accounts:
              return"account not found"
    if amount<=0:
           return"amount be positive"
    if accounts[account_number]['balance'] < amount:
        return "Insufficient balance."
    accounts[account_number][balance]-=amount
    return f"withdraw{amount}successfully.new balance:{accounts[account_number][balance]}"
#check account balance
def check_balance(account_number):
    if account_number not in accounts:
        return "Account does not exist"

    return f"Account Holder: {accounts[account_number]['account_holder']}\nBalance: {accounts[account_number]['balance']}"
#bank managment system
def bank_managment_system():
 print("_______bank managment system")
 print("1.create account")
 print("2.deposite money")
 print("3.withdraw money")
 print("4.check balances")
 print("5.exit program")


while True:
      choice=input("enter your choice(1 to 5):")
      if choice=="1":
        account_number=int(input("enter account number:"))
        account_holder=(input("enter account holder name:"))
        initial_balance=input("enter initial-balance:")
        result=create_account(account_number,account_holder,initial_balance)
        print(result)
      elif choice=="2":
        account_number=int(input("enter account number:"))
        amount=int(input("enter your amount:"))
        result=deposit_money(account_number,amount)
        print(  result)
      elif choice=="3":
        account_number=int(input("enter account number:"))
        amount=int(input("enter your amount:"))
        result=withdraw_money(account_number,amount)
        print(  result)
      elif choice=="4":
        account_number=int(input("enter account number:"))
        result=withdraw_money(account_number)
        print(  result)
      elif choice=="5":
        print("exit program")
        break
      else:
           print("invalid account")

bank_managment_system()  



print("create account")
name = input("enter your name")
age = int(input("enter your age"))
pin = int(input("create your pin"))
phone = input("enter your phone number")
balance = int(input("enter your balance"))

history = []
accounts = {}
account_number = 1000

if age >= 18:
    account_number += 1
    account = {
        "name": name,
        "age": age,
        "account_number": account_number,
        "pin": pin,
        "phone": phone,
        "balance": balance
    }
    accounts[account_number] = account
    print("create account successful")
    print("your account number is", account_number)
else:
    print("you are not 18, you cant create account")

if age >= 18:
    print("login account")
    login_account = int(input("enter your account number"))
    login_pin = int(input("enter your pin"))

    
    if login_account == account["account_number"] and login_pin == account["pin"]:

        print("login successful")
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Account Information")
            print("7. Change PIN")
            print("8. Account Status")
            print("9. Exit")
            option = input("choose option")

            if option == "1":
                deposit = int(input("enter your deposit amount: "))
                if deposit > 0:
                    account["balance"] += deposit
                    history.append(f"Deposit: Rs. {deposit}")
                    print("deposit successful")
                    print("your balance is", account["balance"])
                else:
                    print("no deposit amount")

            elif option == "2":
                withdraw = int(input("enter your withdraw amount: "))
                if withdraw > 0:
                    if withdraw <= account["balance"]:
                        account["balance"] -= withdraw
                        history.append(f"Withdraw: Rs. {withdraw}")
                        print("withdraw successful")
                        print("your balance is", account["balance"])
                    else:
                        print("insufficient balance")
                else:
                    print("invalid amount")

            elif option == "3":
                receiver = int(input("receiver account number"))
                transfer = int(input("transfer amount"))
                if receiver in accounts and receiver != login_account:
                    if transfer > 0 and transfer <= account["balance"]:
                        account["balance"] -= transfer
                        accounts[receiver]["balance"] += transfer
                        history.append(f"From {login_account} to {receiver}: Rs. {transfer}")
                        print("transfer successful")
                        print("your balance:", account["balance"])
                    else:
                        print("invalid amount or insufficient balance")
                else:
                    print("receiver account not found")

            elif option == "4":
                print("your balance is", account["balance"])

            elif option == "5":
                print("Transaction History")
                for transaction in history:
                    print(transaction)
                if len(history) == 0:
                    print("no transactions yet")

            elif option == "6":
                print("Account Information")
                print("Name:", account["name"])
                print("Age:", account["age"])
                print("Account Number:", account["account_number"])
                print("Phone:", account["phone"])

            elif option == "7":
                oldpin = int(input("enter old PIN"))
                if oldpin == account["pin"]:
                    newpin = int(input("create new PIN"))
                    account["pin"] = newpin
                    print("PIN changed successfully")
                else:
                    print("wrong PIN")

            elif option == "8":
                print("Account Status: Active")

            elif option == "9":
                print("Exit")
                print("Thank you for using our ATM Bank")
                breakc

            else:
                print("invalid option")
    else:
        print("wrong account number or PIN")
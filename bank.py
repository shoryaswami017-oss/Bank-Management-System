accounts = {}
next_account = 1001
print("====== BANK MANAGEMENT SYSTEM ======")
password = "admin123"
while True:
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choi = input("Enter your choice (1-3): ")

    if choi == '1':
        print("====== CUSTOMER ======")
        print("1. Create Account")
        print("2. Login")
        print("3. Back")
        y = input("Enter your choice (1-3): ")
        if y == '1':
            name = input("Enter your name: ")
            acc_number = str(next_account)
            accounts[acc_number] = {"Name": name, "Balance": 0}
            print(f"Account created successfully! Your account number is {acc_number}")
            next_account += 1
        elif y == '2':
            acc_number = input("Enter your account number: ")
            if acc_number in accounts:
                while True:
                    print("1. View Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Back")

                    choice = input("Enter your choice (1-4): ")

                    if choice == '1':
                        print(f"Your balance is: {accounts[acc_number]['Balance']}")

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        if amount > 0:
                         accounts[acc_number]['Balance'] += amount
                         print(f"Deposited {amount}. New balance is: {accounts[acc_number]['Balance']}")
                        else:
                            print("Invalid amount. Please enter a positive value.")

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        if amount <= 0: 
                            print("Invalid amount. Please enter a positive value.")
                        elif amount <= accounts[acc_number]['Balance']:
                            accounts[acc_number]['Balance'] -= amount
                            print(f"Withdrew {amount}. New balance is: {accounts[acc_number]['Balance']}")
                        else:
                            print("Insufficient balance.")

                    elif choice == '4':
                        print("You exited from Customer menu!!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Account number not found.")
        elif y == '3':
            print("You exited from Customer menu!!")
            break
        else:
            print("Invalid choice. Please try again.")

    elif choi == '2':
        i = 3
        while i > 0:
            passu = input("Enter Password: ")

            if passu == password:
                while True:
                    print("1. View Accounts")
                    print("2. Search")
                    print("3. Delete")
                    print("4.. Total Accounts")
                    print("5. Back")

                    choicee = input("Enter your choice (1-5): ")

                    if choicee == '1':
                        if len(accounts) == 0:
                            print("No accounts found.")
                        else:
                         for key, value in accounts.items():
                            print(f"{key}: {value}")

                    elif choicee == '2':
                        acc_number = input("Enter the Account number: ")
                        if acc_number in accounts:
                            print(f"{acc_number}: {accounts[acc_number]}")
                        else:
                            print("Account number not found")

                    elif choicee == '3':
                        for i in range(3):
                            x = input("Enter admin password to delete accounts: ")

                            if x == password:
                                del_accnum = input("Enter account number you want to delete: ")

                                if del_accnum in accounts:
                                    accounts.pop(del_accnum)
                                    print("Account Deletion Successful")
                                    break
                                else:
                                    print("Account number not found")
                                    break

                            else:
                                print(f"Incorrect Password !! you have {2-i} more chances left")

                        else:
                            print("Access Denied XX you have used all of your chances")

                    elif choicee == '4':
                        print(f"Total number of accounts are {len(accounts)}")

                    elif choicee == '5':
                        print("You exited from Admin menu!!")
                        break
                    else:
                        print("Invalid choice")
                break
            else :
                i-=1
                print(f"Wrong Password {i} chances left")
                
        else:
            print("Access  Denied!")
    elif choi == '3':
        print("You have successfully exited from Bank Management System")
        break
    else:
        print("Invalid choice. Please try again.")
    
            
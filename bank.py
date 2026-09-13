import json


DATA_FILE = "accounts.json"
ADMIN_PASSWORD = "admin123"


# =========================
# DATA MANAGEMENT
# =========================

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            accounts = data.get("accounts", {})
            next_account = data.get("next_account", 1001)

            return accounts, next_account

    except FileNotFoundError:
        return {}, 1001


def save_data():
    data = {
        "accounts": accounts,
        "next_account": next_account
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# =========================
# CUSTOMER FUNCTIONS
# =========================

def create_account():
    global next_account

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    account_number = str(next_account)

    accounts[account_number] = {
        "Name": name,
        "Balance": 0
    }

    next_account += 1

    save_data()

    print("\nAccount created successfully!")
    print(f"Your account number is: {account_number}")


def customer_login():
    account_number = input("Enter your account number: ").strip()

    if account_number not in accounts:
        print("Account number not found.")
        return

    print(f"\nWelcome, {accounts[account_number]['Name']}!")

    while True:
        print("\n====== CUSTOMER MENU ======")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Back")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_balance(account_number)

        elif choice == "2":
            deposit_money(account_number)

        elif choice == "3":
            withdraw_money(account_number)

        elif choice == "4":
            print("Returning to Customer menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def view_balance(account_number):
    balance = accounts[account_number]["Balance"]

    print(f"Your current balance is: ₹{balance:.2f}")


def deposit_money(account_number):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Please enter a positive amount.")
            return

        accounts[account_number]["Balance"] += amount

        save_data()

        print(f"₹{amount:.2f} deposited successfully.")
        print(
            f"New balance: ₹{accounts[account_number]['Balance']:.2f}"
        )

    except ValueError:
        print("Please enter a valid number.")


def withdraw_money(account_number):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Please enter a positive amount.")
            return

        balance = accounts[account_number]["Balance"]

        if amount > balance:
            print("Insufficient balance.")
            return

        accounts[account_number]["Balance"] -= amount

        save_data()

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(
            f"Remaining balance: ₹{accounts[account_number]['Balance']:.2f}"
        )

    except ValueError:
        print("Please enter a valid number.")


# =========================
# ADMIN FUNCTIONS
# =========================

def admin_login():
    attempts = 3

    while attempts > 0:
        password = input("Enter admin password: ")

        if password == ADMIN_PASSWORD:
            print("\nAdmin login successful!")
            admin_menu()
            return

        attempts -= 1

        if attempts > 0:
            print(f"Wrong password. {attempts} attempt(s) remaining.")
        else:
            print("Access Denied!")


def admin_menu():

    while True:
        print("\n====== ADMIN MENU ======")
        print("1. View All Accounts")
        print("2. Search Account")
        print("3. Delete Account")
        print("4. Total Accounts")
        print("5. Back")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_all_accounts()

        elif choice == "2":
            search_account()

        elif choice == "3":
            delete_account()

        elif choice == "4":
            total_accounts()

        elif choice == "5":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def view_all_accounts():

    if not accounts:
        print("No accounts found.")
        return

    print("\n====== ALL ACCOUNTS ======")

    for account_number, details in accounts.items():

        print(
            f"Account: {account_number} | "
            f"Name: {details['Name']} | "
            f"Balance: ₹{details['Balance']:.2f}"
        )


def search_account():

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:

        details = accounts[account_number]

        print("\nAccount Found!")
        print(f"Account Number: {account_number}")
        print(f"Name: {details['Name']}")
        print(f"Balance: ₹{details['Balance']:.2f}")

    else:
        print("Account number not found.")


def delete_account():

    if not accounts:
        print("No accounts available.")
        return

    password = input("Enter admin password: ")

    if password != ADMIN_PASSWORD:
        print("Incorrect password.")
        return

    account_number = input(
        "Enter account number you want to delete: "
    ).strip()

    if account_number in accounts:

        del accounts[account_number]

        save_data()

        print("Account deleted successfully.")

    else:
        print("Account number not found.")


def total_accounts():

    print(f"Total number of accounts: {len(accounts)}")


# =========================
# MAIN PROGRAM
# =========================

accounts, next_account = load_data()


print("====== BANK MANAGEMENT SYSTEM ======")

while True:

    print("\n1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # CUSTOMER
    if choice == "1":

        while True:

            print("\n====== CUSTOMER ======")
            print("1. Create Account")
            print("2. Login")
            print("3. Back")

            customer_choice = input(
                "Enter your choice (1-3): "
            )

            if customer_choice == "1":
                create_account()

            elif customer_choice == "2":
                customer_login()

            elif customer_choice == "3":
                print("Returning to main menu...")
                break

            else:
                print("Invalid choice. Please try again.")

    # ADMIN
    elif choice == "2":
        admin_login()

    # EXIT
    elif choice == "3":

        print("\nThank you for using Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
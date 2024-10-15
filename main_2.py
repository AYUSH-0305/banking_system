class Bank_account:
    def __init__(self, account_number, name, username, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.username = username
        self.password = password  # Store the password as plain text
        self.balance = balance

    def check_pass(self, password):
        """Verifies the password by comparing it with the stored password."""
        return self.password == password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount!")

    def view_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ₹{self.balance}\n")

    def transfer(self, amount, destination_account):
        """Transfers money to another account if sufficient balance is available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            destination_account.balance += amount
            print(f"₹{amount} transferred successfully to Account {destination_account.account_number}.")
            print(f"New balance: ₹{self.balance}")
        else:
            print("Insufficient funds for transfer!")


# Function to create a new account
def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter account holder's name: ")
    username = input("Choose a username: ")
    password = input("Set a password: ")  # Take password input as normal text
    account = Bank_account(account_number, name, username, password)
    return account

# Function to log in the user
def login(accounts):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for account in accounts.values():
        if account.username == username and account.check_pass(password):
            print("Login successful!")
            return account
    print("Invalid username or password!")
    return None

# Function to find an account by account number
def find_account_by_number(accounts, account_number):
    return accounts.get(account_number, None)

# Main program
def main():
    accounts = {}

    while True:
        print("\nBank Management System")
        print("1. Open a new account")
        print("2. Login to account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print("Account created successfully!")
        elif choice == '2':
            logged_in_account = login(accounts)
            if logged_in_account:
                while True:
                    print("\n1. Deposit money")
                    print("2. Withdraw money")
                    print("3. Check balance")
                    print("4. Transfer money to another account")
                    print("5. Logout")

                    action = input("Enter your choice: ")

                    if action == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        logged_in_account.deposit(amount)
                    elif action == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        logged_in_account.withdraw(amount)
                    elif action == '3':
                        logged_in_account.view_balance()
                    elif action == '4':  # Transfer money to another account
                        destination_acc_number = input("Enter destination account number: ")
                        destination_account = find_account_by_number(accounts, destination_acc_number)
                        if destination_account:
                            amount = float(input("Enter the amount to transfer: "))
                            logged_in_account.transfer(amount, destination_account)
                        else:
                            print("Destination account not found!")
                    elif action == '5':
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice, please try again!")
        elif choice == '3':
            print("Thank you for using the Bank Management System!")
            break
        else:
            print("Invalid choice, please try again!")

main()

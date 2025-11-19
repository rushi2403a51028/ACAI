class BankAccount:
    # Constructor to initialize account holder's name and starting balance
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. - task_5.py:11")
        else:
            print("Deposit amount must be positive. - task_5.py:13")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive. - task_5.py:18")
        elif amount > self.balance:
            print("Insufficient funds. - task_5.py:20")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. - task_5.py:23")

    # Method to check current account balance
    def check_balance(self):
        print(f"{self.name}'s current balance: ₹{self.balance} - task_5.py:27")

# Main function to interact with the user
def main():
    # Ask for account holder's name
    name = input("Enter account holder's name: ")
    
    try:
        # Ask for initial balance and create account
        initial_balance = float(input("Enter initial balance: "))
        account = BankAccount(name, initial_balance)

        # Loop to allow multiple operations until user exits
        while True:
            print("\nChoose an option: - task_5.py:41")
            print("1. Deposit - task_5.py:42")
            print("2. Withdraw - task_5.py:43")
            print("3. Check Balance - task_5.py:44")
            print("4. Exit - task_5.py:45")
            choice = input("Enter your choice (1-4): ")

            # Perform action based on user's choice
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                print("Thank you for banking with us! - task_5.py:58")
                break
            else:
                print("Invalid choice. Please select from 1 to 4. - task_5.py:61")
    
    # Handle non-numeric input gracefully
    except ValueError:
        print("Invalid input. Please enter numeric values for balance and transactions. - task_5.py:65")

# Run the main function
main()

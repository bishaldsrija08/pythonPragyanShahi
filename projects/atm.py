balance = 500

def menu():
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print(f"Your current balance is: {balance}")
    
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    balance += amount # balance = balance + amount

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount # balance = balance - amount

def main():
    menu()
    while True:
        choice = input("Please select an options (1-4): ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")

main()
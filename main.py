# main.py
from account import create_account, check_balance
from operations import deposit, withdraw
from history import add_to_history, show_history
from data_manager import save_data, load_data

def main():
    account, balance, history = load_data()

    while True:
        choice = input("\nWelcome to Python Bank!\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History\n6. Exit\nPlease select an option: ")
        if not choice.isdigit() or not (1 <= int(choice) <= 6):
            print("Invalid input, please enter a number between 1 and 6.")
            continue

        choice = int(choice)
        match choice:
            case 1:
                if account is None:
                    account = create_account()
                else:
                    print("An account already exists!")
            case 2:
                if account:
                    amount = float(input("Enter the amount to deposit: "))
                    balance = deposit(balance, amount)
                    add_to_history(history, f"Deposit: ${amount}")
                else:
                    print("No account exists. Please create one first.")
            case 3:
                if account:
                    amount = float(input("Enter the amount to withdraw: "))
                    balance = withdraw(balance, amount)
                    add_to_history(history, f"Withdrawal: ${amount}")
                else:
                    print("No account exists. Please create one first.")
            case 4:
                check_balance(account, balance)
            case 5:
                show_history(history)
            case 6:
                save_data(account, balance, history)
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()
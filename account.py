# account.py
def create_account(first_name: str = None, last_name: str = None, id_number: str = None, initial_balance: float = 0.0):
    if first_name is None or last_name is None or id_number is None:
        first_name = input("Enter your first name: ").capitalize()
        last_name = input("Enter your last name: ").capitalize()
        id_number = input("Enter your ID number: ")
    account = {"first_name": first_name, "last_name": last_name, "ID": id_number, "balance": initial_balance}
    print(f"Account created for {first_name} {last_name} with ID {id_number}. Starting balance: ${initial_balance}")
    return account

def check_balance(account, balance):
    if account:
        print(f"{account['first_name']} {account['last_name']}, your current balance is: ${balance}")
    else:
        print("No account exists.")
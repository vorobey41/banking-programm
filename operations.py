# operations.py
def deposit(balance: float, amount: float):
    if amount > 0:
        new_balance = balance + amount
        print(f"Deposited: ${amount}. New balance: ${new_balance}")
        return new_balance
    else:
        print("Invalid deposit amount.")
        return balance

def withdraw(balance: float, amount: float):
    if amount > balance:
        print(f"Insufficient funds! Current balance is ${balance}.")
    elif amount <= 0:
        print("Invalid withdrawal amount.")
    else:
        new_balance = balance - amount
        print(f"Withdrew: ${amount}. New balance: ${new_balance}")
        return new_balance
    return balance
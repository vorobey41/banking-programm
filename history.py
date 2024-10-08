# history.py
def add_to_history(history, transaction):
    history.append(transaction)

def show_history(history):
    if history:
        print("Transaction History:")
        for index, transaction in enumerate(history, 1):
            print(f"{index}. {transaction}")
    else:
        print("No transaction history available.")
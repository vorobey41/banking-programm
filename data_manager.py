# data_manager.py
import json

def save_data(account, balance, history, filename="bank_data.json"):
    with open(filename, 'w') as file:
        data = {
            "account": account,
            "balance": balance,
            "history": history
        }
        json.dump(data, file)
    print("Data saved successfully.")

def load_data(filename="bank_data.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("Data loaded successfully.")
            return data.get("account"), data.get("balance", 0), data.get("history", [])
    except FileNotFoundError:
        print("No previous data found. Starting with a new session.")
        return None, 0.0, []
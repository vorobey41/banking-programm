Python Banking Program 💰
A simple command-line banking application written in Python, designed to manage basic bank account operations. This project demonstrates essential programming concepts, including modularization, data validation, and file handling. The application allows users to create and manage bank accounts, perform transactions, and track account history.

Features
Account Management: Create an account with your name and ID, and check your account balance anytime.
Transactions:
Deposit: Add funds to your account.
Withdraw: Take funds from your account, with checks to prevent overdrafts.
Transaction History: View a detailed history of all deposits and withdrawals.
Data Persistence: Account information, balance, and transaction history are saved to a file when you exit, allowing you to continue from where you left off next time.
Project Structure
The program is split into several modules for better organization and maintainability:

main.py: The main entry point for the application, managing the primary user interface and calling functions from other modules.
account.py: Handles account creation and balance checking.
operations.py: Manages deposit and withdrawal operations.
history.py: Manages transaction history, including adding new transactions and viewing past transactions.
data_manager.py: Responsible for loading and saving account data to a JSON file, ensuring data persistence between sessions.
Requirements
Python 3.6+
No external libraries are required; all functionalities are implemented with Python’s standard library.

Getting Started
Clone the Repository:
bash
git clone https://github.com/yourusername/python-banking-program.git
cd python-banking-program
Run the Application:

bash
python main.py
Usage
After starting the program, you will see a menu with the following options:

Create Account: Set up a new account with your name, ID, and initial balance.
Deposit: Deposit funds into your account.
Withdraw: Withdraw funds from your account.
Check Balance: Display your current account balance.
Transaction History: View your full transaction history.
Exit: Save all data and exit the program.
Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

# Python Banking Program 💰

A simple command-line banking application written in Python for managing basic bank account operations. This project demonstrates essential programming concepts, including modularization, data validation, and file handling.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Account Management**: Create an account with your name and ID, and view your balance.
- **Transactions**: 
  - **Deposit**: Add funds to your account.
  - **Withdraw**: Withdraw funds with overdraft prevention.
- **Transaction History**: View all deposits and withdrawals.
- **Data Persistence**: Account information, balance, and transaction history are saved to a file when you exit, allowing you to resume where you left off.

## Project Structure
The program is split into several modules for better organization and maintainability:

- `main.py`: Main entry point, managing the primary user interface.
- `account.py`: Handles account creation and balance checking.
- `operations.py`: Manages deposit and withdrawal operations.
- `history.py`: Manages transaction history, including adding and viewing records.
- `data_manager.py`: Loads and saves account data to a JSON file for data persistence.

## Requirements
- Python 3.6+
- No external libraries required; all functionalities are implemented with Python’s standard library.

## Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vorobey41/banking-programm.git
   cd banking-programm

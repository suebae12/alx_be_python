# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Default starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    command_parts = command_input.split(':')

    command = command_parts[0]
    try:
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except ValueError:
        print("Invalid amount format. Please use a valid number.")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

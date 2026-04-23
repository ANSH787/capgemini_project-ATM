import account
import storage
import transaction
import validator


GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


def line():
    print(CYAN + "=" * 40 + RESET)


def display_balance():
    line()
    print(f"{CYAN}   CURRENT BALANCE{RESET}")
    line()
    print(f"{GREEN}   ₹ {account.balance}{RESET}")
    line()


def deposit():
    line()
    print("   DEPOSIT MONEY")
    line()

    amount = float(input("Enter amount: "))

    if not validator.is_valid_amount(amount):
        print(RED + "Invalid amount" + RESET)
        return

    account.balance += amount
    txn = transaction.make_transaction("Deposit", amount)
    storage.add_transaction(txn)

    print(GREEN + "Deposit successful" + RESET)


def withdraw():
    line()
    print("   WITHDRAW MONEY")
    line()

    amount = float(input("Enter amount: "))

    if not validator.is_valid_amount(amount):
        print(RED + "Invalid amount" + RESET)
        return

    if amount > account.balance:
        print(RED + "Insufficient balance" + RESET)
        return

    account.balance -= amount
    txn = transaction.make_transaction("Withdraw", amount)
    storage.add_transaction(txn)

    print(GREEN + "Withdrawal successful" + RESET)


def show_statement():
    line()
    print("   TRANSACTION HISTORY")
    line()

    txns = storage.get_transactions()

    if not txns:
        print(RED + "No transactions yet" + RESET)
        return

    for i, t in enumerate(txns, 1):
        print(f"{i}. {t}")

    line()
import atm_service

def menu():
    print("\n" + "=" * 40)
    print("         💳 ATM SYSTEM")
    print("=" * 40)
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")
    print("=" * 40)


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        atm_service.display_balance()

    elif choice == "2":
        atm_service.deposit()

    elif choice == "3":
        atm_service.withdraw()

    elif choice == "4":
        atm_service.show_statement()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
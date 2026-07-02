balance = 0

while True:
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Amount deposited successfully")

        case 2:
            if balance == 0:
                print("No balance available. Please deposit first")
            else:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance = balance - amount
                    print("Withdrawal successful")
                else:
                    print("Insufficient balance")

        case 3:
            if balance == 0:
                print("No balance available. Please deposit first")
            else:
                print("Current Balance:", balance)

        case 4:
            if balance == 0:
                print("No balance available. Please deposit first")
            else:
                if balance > 50000:
                    interest = balance * 0.05
                else:
                    interest = balance * 0.03

                balance = balance + interest
                print("Interest added:", interest)
                print("Updated Balance:", balance)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

    again = input("DO YOU WANT TO CONTINUE (YES / NO): ").lower()

    match again:
        case "yes":
            continue
        case "no":
            break
        case _:
            print("PLEASE CHOOSE APPROPRIATE OPTION")
            break
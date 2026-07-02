a = None
hra = 0
da = 0
netsalary = 0
tax = 0
finalsalary = 0

while True:
    print("1. Enter Basic Salary")
    print("2. Calculate HRA (20%) and DA (10%)")
    print("3. Calculate Net Salary")
    print("4. Tax Deduction")
    print("5. Display Salary Slip")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            a = int(input("Enter Basic Salary: "))
            print("Basic Salary recorded successfully")

        case 2:
            if a is None:
                print("Please enter basic salary first")
            else:
                hra = 0.20 * a
                da = 0.10 * a
                print("HRA:", hra)
                print("DA:", da)

        case 3:
            if a is None:
                print("Please enter basic salary first")
            else:
                hra = 0.20 * a
                da = 0.10 * a
                netsalary = a + hra + da
                print("Net Salary (before tax):", netsalary)

        case 4:
            if a is None:
                print("Please enter basic salary first")
            else:
                hra = 0.20 * a
                da = 0.10 * a
                netsalary = a + hra + da

                if netsalary > 50000:
                    tax = 0.10 * netsalary
                else:
                    tax = 0.05 * netsalary

                print("Tax Deduction:", tax)

        case 5:
            if a is None:
                print("Please enter basic salary first")
            else:
                hra = 0.20 * a
                da = 0.10 * a
                netsalary = a + hra + da

                if netsalary > 50000:
                    tax = 0.10 * netsalary
                else:
                    tax = 0.05 * netsalary

                finalsalary = netsalary - tax

                print(f"Basic Salary : {a} HRA: {hra} DA: {da} Net Salary: {netsalary} Tax: {tax} Final Salary: {finalsalary}")

        case 6:
            print("Exiting program... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")

    again = input("Do you want to continue (yes/no): ").lower()

    match again:
        case "yes":
            continue

        case "no":
            print("Exiting program... Thank you!")
            break

        case _:
            print("Choose appropriate option")
            break
balance = int(input("Deposit first: "))

while True:
    print("\n Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    selection = int(input("\n Enter your selection here: "))
    
    if selection == 1:
        deposit = int(input("Enter the Amount you want to Deposit: "))
        balance += deposit
        print(f'You Deposited an amount of {deposit} your total balance is {balance}')
    elif selection == 2:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw > balance:
            print("Insufficient Fund")
        else:
            balance -= withdraw
            print(f"You have successfully withdrawn an amount of {withdraw} your total balance is {balance}")
    elif selection == 3:
        print(f"Your total balance is {balance}")
    elif selection == 4:
        print("thanks for using our banking system")
        break
    else:
        print("Invalid selection")
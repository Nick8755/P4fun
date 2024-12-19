def deposit ():
    while True:
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            break
        else:
            print("Invalid amount. Amount must be greater than 0. Please try again.")
    return amount

deposit()
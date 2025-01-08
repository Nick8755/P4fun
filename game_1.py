MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit ():
    while True:
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            break
        else:
            print("Invalid amount. Amount must be greater than 0. Please try again.")
    return amount

def get_number_of_lines():
    while True:
        lines = int(input("Enter the number of lines: "))
        if lines > 0 and lines <= MAX_LINES:
            break
        else:
            print(f"Invalid number of lines. Number of lines must be between 1 and {MAX_LINES}. Please try again.")
    return lines

def get_bet_amount(balance):
    while True:
        bet = int(input("Enter the bet amount on each line: "))
        if bet > balance:
            print(f"Insufficient balance. Bet amount must be less than or equal to your balance of {balance}. Please try again.")
        elif bet >= MIN_BET and bet <= MAX_BET:
            break
        else:
            print(f"Invalid bet amount. Bet amount must be between {MIN_BET} and {MAX_BET}. Please try again.")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet_amount(balance)
    total_bet = lines * bet
    print(f"Your balance is: {balance} and the number of lines is: {lines}")
    print(f"Your bet amount is: {bet} on {lines} lines. Total bet amount is: {total_bet}")

main()


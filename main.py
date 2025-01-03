#import modules
import random

#global constant
MAX_LINES  = 3
MAX_BET = 100
MIN_BET = 1

#specify rows n column
ROWS =3
COLS =3

#specify symbols for each wheel (column)
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #look only thru lines that are betted on
    for line in range(lines):
        #check for first symbol in column
        symbol = columns[0][line]
        #loop thru every column and check for match
        for column in columns:
            symbol_to_check = column[line]
            #if symbol is not a match
            if symbol != symbol_to_check:
                break
        else:
            #if all symbols are the same + user won the bet
            #add the winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1 )

    return winnings, winning_lines


#Generate outcome of bet according to symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #add symbols to list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    #create a selection
    # the nested list repersent each selection
    columns = []
    for _ in range(cols):
        column = []
        #copy list ":" so each column has its own selection
        current_symbols = all_symbols[:]
        for _ in range(rows):
            #select value
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            #add value to column
            column.append(value)

        columns.append(column)

    return columns

#test and print
def print_slot_machine(columns):
    #transpose the format of our results
    for row in range(len(columns[0])):
        #point to first value of selection
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
        else:
            print(column[row])
    print()
    

#collect user input
def deposit():
    #continue  to ask for input until user enters a valid number
    while True:
        amount  = input("What would you like to deposit $$$: ")
        #verify numerical value w isdigit method 
        if  amount.isdigit():
            #convert string to integer
            amount = int(amount)
            #verify int is greater than 0
            if amount > 0:
                break  
            else:
                 print("Please enter a valid amount greater than 0")   
        else:
            print("Please enter a valid number")
    return amount

def get_number_of_lines():
    #pick int between 1  and 3
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +  ")? " )
        if   lines.isdigit():
            lines  = int(lines)
            if 1  <=  lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and 3")
        else:
            print("Please enter a valid number")
    return lines

#amount to bet on each line
def get_bet():
    while True:
        amount =  input("What are you betting on  each line ? ($" + str(MIN_BET) + " - $" + str(MAX_BET) + "): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Please enter a valid amount between " + str(MIN_BET) + " and " + str(MAX_BET))
        else:
            print("Please enter a valid number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    #Verify the bet amount is within limit of available balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to make that bet. Your current balance is ${balance}")
        else:
            break
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    #print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print("you won on lines: ", *winning_lines)
    return winnings - total_bet


def main():    
    balance  = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("Press enter to play. q to quit")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

   
main()

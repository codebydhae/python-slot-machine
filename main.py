#global constant
MAX_LINES  = 3
MAX_BET = 100
MIN_BET = 1

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

def main():    
    balance  = deposit()
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

main()

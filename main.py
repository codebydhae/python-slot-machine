#global constant
MAX_LINES  = 3

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

def main():    
    balance  = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()

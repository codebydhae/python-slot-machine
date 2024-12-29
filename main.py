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
    


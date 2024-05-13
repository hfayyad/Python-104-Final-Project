"""

Comments
 Python 104 Final project. Follow prompts on terminal. Review code.
 When Y is inputted on terminal, it prompts another. Please clear after every cycle.
 Loop happen after every action completed or abort.
"""





import decimal


tsla = 219.27  #Price for stock to determine buy or sell
ipo = 1.28  #Inital Public offering price for background knowledgo
name = "TSLA" #name for console
date = "7/2/10" #date of ipo
current_price = decimal.Decimal(219.27) #price for stock
nasdaqinfo = ["Insert 'NASDAQ INFO'", "$TSLA"] #variable for all to print
price_beginning_of_day = decimal.Decimal(224.44) #price in the beginning of day
price_end_of_day = decimal.Decimal(219.27) #price at end

"""=================Greeting======================"""
def Info():
    print ("Welcome to Hamza's Trading Bot! Please refer to the variables above and update if nessacary") #for user, this prints in console for use
Info()
print (nasdaqinfo[1])
"""=================Greeting======================"""


if (current_price < price_beginning_of_day):
    print ("Please select desired value to sell")
else:
    print ("Please wait until price is above current price")
# if price is higher than in the beginning, move to next prompt and select, if not prompt pops up to wait

loop = True
# loop is to restart the program after it starts for continued use, numbers are example numbers in practice it would be live
while loop:
#inputs, double checking to confirm, aborting if not 
    print (tsla, "Y/N")
    x = input()
 #elif for Y
    if x == 'Y':
        print("Double check you chose the correct option")

#elif for N
    elif x == 'N':    
        print("Double check you chose the correct option")

    else:
        print ('Wrong input')
#code for Y/N inputs
    print ("Y/N")
    x = input ()
    if x == 'Y':
        print("Action completed")
        tsla +=1
    elif x == 'N':    
        print("Aborting actions and returning to first step")
        tsla +=1
    else:
        print ('Wrong input')
    
loop: False
#

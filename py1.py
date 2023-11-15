"""

Comments
 Python 104 Final project. Follow prompts on terminal. Review code.
 When Y is inputted on terminal, it prompts another. Please clear after every cycle.
 Loop happen after every action completed or abort.
"""





import decimal


tsla = 219.27
ipo = 1.28
name = "TSLA"
date = "7/2/10"
current_price = decimal.Decimal(219.27)
nasdaqinfo = ["Insert 'NASDAQ INFO'", "$TSLA"]
price_beginning_of_day = decimal.Decimal(224.44)
price_end_of_day = decimal.Decimal(219.27)

"""=================Greeting======================"""
def Info():
    print ("Welcome to Hamza's Trading Bot! Please refer to the variables above and update if nessacary")
Info()
print (nasdaqinfo[1])
"""=================Greeting======================"""


if (current_price < price_beginning_of_day):
    print ("Please select desired value to sell")
else:
    print ("Please wait until price is above current price")



loop = True

while loop:

    print (tsla, "Y/N")
    x = input()
    if x == 'Y':
        print("Double check you chose the correct option")


    elif x == 'N':    
        print("Double check you chose the correct option")

    else:
        print ('Wrong input')

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

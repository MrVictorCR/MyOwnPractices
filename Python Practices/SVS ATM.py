"""
    In this program you will be able to see an ATM console program.
    This will have different options in order for you to do your business
    
    I decided to practice different topics with this program:
        Functions
        Conditionals
        Exceptions, so on

    I will add other options that we could be able to do in an ATM machine
    That would be in future versions
"""

#- Vars that I need in the program -#

balance = 0
y = 0
z = bool

#-----------------------------------#

#- Main Menu: Displays the options that the ATM is going to have -#

def menu():

    try: 
         x = int(input(f"""
1. To Deposit money in your account
2. To withdraw money from your account
3. To see the balance in your account
---------------------------------------- """))
        
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
    
    finally:
        return x

#-----------------------------------------------------------------#

#- Adding ATM Functions -#

def deposit(balance, y):
    balance += y
    print(f"\n\tThe available balance in the account is {balance}$\n")
    return balance

def withdraw(balance, y):
    
    if balance < y:
        print("""
We apologize for the inconvenience but right now,
The available balance is less than what you want to withdraw""")
        
    else:
        balance -= y
    print(f"\n\tThe available balance in the account is {balance}$\n")
    return balance

def show(balance):
    print(f"\n\tThe available balance in the account is {balance}$\n")

#------------------------#

#- "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" -#

def secMenu():
    try:
        print("Do you want to do something else?")
        c = int(input("1. Yes\n" +
                            "2. Exit\n------- "))

        if c == 1:
            z = True
        elif c == 2:
            print("\nThank you for using our services!\n\t" +
                  "Enjoy the rest of your day :) \n\t")
            z = False
        else:
            raise ValueError ("Error -> The Option you chosee doesn't exist \n")
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        z = True

    finally:
        return z

#--------------------------------------------------------------------------------------------------------------#

#- MAIN PROGRAM -# 

print("\n\tWelcome to SVS ATM")

#- Loop Call -#
while(z):

    #- Menu Call -#
    x = menu()

    try:

        if x == 1:
            y = int(input("""
What would be the amount that you want to deposit?
--------- """))
            balance = deposit(balance, y)

        elif x == 2:
            y = int(input("""
What would be the amount that you want to withdraw?
--------- """))
            balance = withdraw(balance, y)

        elif x == 3:
            show(balance)

        else:
            raise ValueError ("Error -> The Option you chosee doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        z = secMenu()

#----------------#

#-    E n d    -#
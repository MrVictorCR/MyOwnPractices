"""
    In this program you will be able to see an ATM console program.
    This will have different options in order for you to do your business
    
    I decided to practice different topics with this program:
        Functions
        Conditionals
        Exceptions, so on

    What I'm going to add will be a different function that is going to work as if you want to create a bank account
    So firstable, 2 different menus: create an account - use the ATM Machine
    The ATM machine is already created, so, we need to create the main menu, then the function regarding to create an account

    Create account:
        Import random
        Create an account number randomly (random.choice(x number list))
        Save the name
        Provide with the debit card number, exp date, cvv, so on
"""

import random

# - Vars that I need in the program -#

balance = 0
y = 0
z = bool
numbers = '12345678901234567890'
customers = []
customersDebitCards = []
exitOption = False

# -----------------------------------#

# - Main Menu: Displays the options that the ATM is going to have -#


def mainMenu():

    try:
        option = int(input(f"""
1. To Use the Banking Options
2. To Use the ATM Function
3. Exit
-------------------------- """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return option

# -----------------------------------------------------------------#

# - Bank Menu: Displays the options that the Bank is going to have -#


def bankMenu():

    try:
        option = int(input(f"""
1. To Create a Bank Account
2. To Request for a Debit Card
3. To See your Information
------------------------------ """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return option

# ------------------------------------------------------------------#


# - ATM Menu: Displays the options that the ATM is going to have -#


def atmMenu():

    try:
        option = int(input(f"""
1. To Deposit money in your account
2. To withdraw money from your account
3. To see the balance in your account
---------------------------------------- """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return option

# -----------------------------------------------------------------#

# - Adding Bank Functions -#


def createAccountNumber(iD, name, lastName):

    customerDict = {}

    long = 9
    randomNumbers = random.sample(numbers, long)
    accountNumber = "".join(randomNumbers)

    customerDict['ID'] = iD
    customerDict['Name'] = name
    customerDict['Last Name'] = lastName
    customerDict['Account Number'] = accountNumber

    customers.append(customerDict)


def id_already_exist(iD):

    if len(customers) == 0:
        idAlreadyExist = False
    else:
        for i in customers:
            if i['ID'] == iD:
                idAlreadyExist = True
            else:
                idAlreadyExist = False

    return idAlreadyExist


def createDebitCardNumber(iD):

    if id_already_exist(iD):

        debitCardDict = {}

        for i in customers:
            if i['ID'] == iD:
                cx = (
                    f"{i['Name']}, {i['Last Name']}, {i['Account Number']}")

                long = 16
                randomNumbers = random.sample(numbers, long)
                debitCardNumber = "".join(randomNumbers)

                debitCardDict['ID'] = iD
                debitCardDict['Customer'] = cx
                debitCardDict['Debit Card Number'] = debitCardNumber

                customersDebitCards.append(debitCardDict)
                print('Debit Card added')
    else:

        print("The customer doesn't exits")


def seeYourInfo(iD):
    for i in customersDebitCards:
        if i['ID'] == iD:
            info = (
                f"ID: {i['ID']}, {i['Customer']}, {i['Debit Card Number']}")
            # Customer is not an INT is a List, so I need to get access to the first place!,  Is not getting access to the first position
            # SAVE ID IN A DIFFERENT WAY FOR ME TO GET THE INFO WITHOUT A PROBLEM

            return info

    return False

# -------------------------#

# - Adding ATM Functions -#


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

# ------------------------#

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" -#


def secMenu():
    try:
        print("\nDo you want to do something else?")
        c = int(input("1. Yes\n" +
                      "2. Exit\n------- "))

        if c == 1:
            z = True
        elif c == 2:
            print("\nThank you for using our services!\n\t" +
                  "Enjoy the rest of your day :) \n\t")
            z = False
        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        z = True

    finally:
        return z

# --------------------------------------------------------------------------------------------------------------#

# - MAIN PROGRAM -#


print("\n\tWelcome to SVS ATM")

# - Loop Call -#
while (z):

    # - Menu Call -#
    x = mainMenu()

    try:
        if x == 1:
            option = bankMenu()
            if option == 1:

                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))
                if id_already_exist(iD):
                    print('There is a Customer already added with that ID')

                else:
                    name = input('\nWhat is your First Name?\n' +
                                 '-------------------- ')
                    lastName = input('\nWhat is your Last Name?\n' +
                                     '-------------------- ')
                    createAccountNumber(iD, name, lastName)

            elif option == 2:
                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))
                createDebitCardNumber(iD)

            elif option == 3:
                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))

                info = seeYourInfo(iD)

                if info == False:
                    print('Customer does not exist')
                else:
                    print('\nCustomer founded')
                    print(info)
            else:
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

        if x == 2:
            option = atmMenu()

            if x == 1:
                y = (input("""
        What would be the amount that you want to deposit?
        --------- """))
                if y != int:
                    raise ValueError(
                        "Error -> The Amount should be in numbers \n")
                else:
                    balance = deposit(balance, y)

            elif x == 2:
                y = int(input("""
        What would be the amount that you want to withdraw?
        --------- """))
                balance = withdraw(balance, y)

            elif x == 3:
                show(balance)

            else:
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")
        if x == 3:
            print("\n\tThank you for using our services!\n" +
                  "\tEnjoy the rest of your day :) \n")
            exitOption = True

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:

        if exitOption == True:
            break
        else:
            z = secMenu()

# ----------------#

# -    E n d    -#

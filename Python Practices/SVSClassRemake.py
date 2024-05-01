import random

# - Vars that I need in the program -#

balance = 0
xAmount = 0
loop = bool
numbers = '12345678901234567890'
customersDebitCards = []
customers = []
mbrATMInfo = []
exitOption = False


# - Trying to implement a Class - #

class CreateMember():
    def __init__(self, iD, name, lastName):
        self.iD = iD
        self.name = name
        self.lastName = lastName

# - Create Member Account - #
    def saveMemberAccount(self):
        customersDict = {}
        long = 9
        randomNumbers = random.sample(numbers, long)
        accountNumber = "".join(randomNumbers)

        customersDict['ID'] = self.iD
        customersDict['Name'] = self.name
        customersDict['Last Name'] = self.lastName
        customersDict['Account Number'] = accountNumber
        customers.append(customersDict)

        print('Customer Account created, your account number is: ' + accountNumber)

# - Create Member Card - #
    def createDebitCard(self, iD):

        debitCardsDict = {}

        for i in customers:
            if i['ID'] == iD:
                mbrName = i['Name']
                accountNumber = i['Account Number']

                long = 16
                randomNumbers = random.sample(numbers, long)
                debitCardNumber = "".join(randomNumbers)

                debitCardsDict['ID'] = iD
                debitCardsDict['Customer'] = mbrName
                debitCardsDict['Account Number'] = accountNumber
                debitCardsDict['Debit Card Number'] = debitCardNumber

                customersDebitCards.append(debitCardsDict)
                print(mbrName + " your Debit Card was created" +
                      ' Your debit card number is: ' +
                      debitCardNumber)

# - See Ourself Info - #
    def seeYourInfo(self, iD):
        for i in customers:
            if i['ID'] == iD:
                info = (
                    f"ID: {i['ID']}, Name: {i['Name']} {i['Last Name']}, Account Number: {i['Account Number']}")

                for i in customersDebitCards:
                    if i['ID'] == self.iD:
                        info = (
                            info + f"Card Number: {i['Debit Card Number']}")
                return info
        return False

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

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" -#


def secMenu():
    try:
        print("\nDo you want to do something else?")
        c = int(input("1. Yes\n" +
                      "2. Exit\n------- "))

        if c == 1:
            loop = True
        elif c == 2:
            print("\nThank you for using our services!\n\t" +
                  "Enjoy the rest of your day :) \n\t")
            loop = False
        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        loop = True

    finally:
        return loop

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

# - Adding ATM Functions - #


def researchMember(iD):
    iD = iD
    conditional, mbrName = idMbrDebitCardExist(iD)
    if conditional == False:
        executingFunction = False
        mbrATMAlreadyExist = False
    else:
        print('\nCustomer found\n' +
              'Welcome back ' + mbrName)
        executingFunction = True
        mbrATMAlreadyExist = False

    return mbrATMAlreadyExist, executingFunction, iD, mbrName


def researchATMMember():
    print('\nFirstable you need to provide your information in order to pull up your account')
    iD = int(input('\nWhat is your ID?\n' +
                   '-------------------- '))
    if len(mbrATMInfo) > 0:
        for i in mbrATMInfo:
            if i['ID'] == iD:
                mbrName = i['Member']
                mbrATMAlreadyExist = True
                executingFunction = False
                return mbrATMAlreadyExist, executingFunction, iD, mbrName

    print('Starting first deposit option')
    if len(mbrATMInfo) == 0:

        mbrATMAlreadyExist, executingFunction, iD, mbrName = researchMember(iD)
        return mbrATMAlreadyExist, executingFunction, iD, mbrName
    else:
        mbrATMAlreadyExist, executingFunction, iD, mbrName = researchMember(iD)
        return mbrATMAlreadyExist, executingFunction, iD, mbrName


def deposit(iD, amount):
    for i in mbrATMInfo:
        if i['ID'] == iD:
            balance = i['Balance']
            i['Balance'] = balance + amount
            print(
                f"\n\tThe available balance in the account is: {i['Balance']}$\n")


def firstTimeDeposit(iD, mbrName, balance, xAmount):
    atmDict = {}

    balance += xAmount
    print(f"\n\tThe available balance in the account is {balance}$\n")

    atmDict['ID'] = iD
    atmDict['Member'] = mbrName
    atmDict['Balance'] = balance

    mbrATMInfo.append(atmDict)


def withdraw(amount, iD):

    for i in mbrATMInfo:
        if i['ID'] == iD:

            balance = i['Balance']
            if balance > amount:
                i['Balance'] = balance - amount
                print(
                    f"\n\tThe available balance in the account is: {i['Balance']}$\n")
            else:
                print(f"""
We apologize for the inconvenience but right now,
The available balance is less than what you want to withdraw
Your balance right now is: {i['Balance']}$""")
        else:
            print('Member not founded')


def showBalance(iD):
    for i in mbrATMInfo:
        if i['ID'] == iD:
            print(
                f"\n\tThe available balance in the account is: {i['Balance']}$\n")

# ------------------------ #

# - General Functions - #

# SEE WHAT THIS SHIT IS RETURNING


def idCustomerExist(iD):
    if len(customers) == 0:
        idCustomer = False
    else:
        for i in customers:
            if i['ID'] == iD:
                idCustomer = True
                return idCustomer
            else:
                idCustomer = False
    return idCustomer


def idMbrDebitCardExist(iD):
    if len(customersDebitCards) == 0:
        idCustomerCard = False
    else:
        for i in customersDebitCards:
            if i['ID'] == iD:
                mbrName = (f"{i['Customer']}")
                idCustomerCard = True
                return idCustomerCard, mbrName
            else:
                idCustomerCard = False
                mbrName = ''
    return idCustomerCard, mbrName

# -----------------------#

#

# - MAIN PROGRAM -#


print("\n\tWelcome to SVS ATM")

# - Loop Call -#
while (loop):

    # - Menu Call -#
    optMenu = mainMenu()

    try:
        if optMenu == 1:
            option = bankMenu()
            if option == 1:

                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))
                if idCustomerExist(iD):
                    print('There is a Customer already added with that ID')

                else:
                    name = input('\nWhat is your First Name?\n' +
                                 '-------------------- ')

                    lastName = input('\nWhat is your Last Name?\n' +
                                     '-------------------- ')
                    mbr = CreateMember(iD, name, lastName)
                    mbr.saveMemberAccount()

            elif option == 2:
                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))
                if idCustomerExist(iD):
                    mbr.createDebitCard(iD)
                else:
                    print("The customer doesn't exits")

            elif option == 3:
                iD = int(input('\nWhat is your ID?\n' +
                               '-------------------- '))
                iDCondition, mbrName = idMbrDebitCardExist(iD)
                if iDCondition:
                    info = mbr.seeYourInfo(iD)
                    if info == False:
                        print('Customer does not exist')
                    else:
                        print('\nCustomer founded')
                        print(info)
            else:
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

        """ Start with elif option 2: """
        if optMenu == 2:
            option = atmMenu()

            if option == 1:
                mbrATMAlreadyExist, executingFunction, iD, mbrName = researchATMMember()
                if mbrATMAlreadyExist == True:
                    print('\nWelcome back ' + mbrName)
                    amount = int((input("""
What would be the amount that you want to deposit into your account?
--------- """)))
                    if amount > 0:
                        deposit(iD, amount)
                    else:
                        raise ValueError(
                            'Error -> The Amount should be in numbers \n')

                elif executingFunction == True:
                    amount = int((input("""
What would be the amount that you want to deposit into your account?
--------- """)))
                    if amount > 0:
                        firstTimeDeposit(iD, mbrName, balance, amount)
                    else:
                        raise ValueError(
                            'Error -> The Amount should be in numbers \n')
                else:
                    print('\nThere is not a customer added with that ID\n')

            elif option == 2:
                mbrATMAlreadyExist, executingFunction, iD, mbrName = researchATMMember()
                if (executingFunction == True) or (mbrATMAlreadyExist == True):
                    amount = int(input("""
What would be the amount that you want to withdraw?
--------- """))
                    if amount > 0:
                        withdraw(amount, iD)
                    else:
                        raise ValueError(
                            'Error -> The Amount should be in numbers \n')
                else:
                    print('\nThere is not a customer added with that ID\n')

            elif option == 3:
                mbrATMAlreadyExist, executingFunction, iD, mbrName = researchATMMember()
                if (executingFunction == True) or (mbrATMAlreadyExist == True):
                    showBalance(iD)
                else:
                    print("Member not founded")
            else:
                raise ValueError(
                    'Error -> There is not option with the number you typed\n')
        if optMenu == 3:
            print("\n\tThank you for using our services!\n" +
                  "\tEnjoy the rest of your day :) \n")
            exitOption = True

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        if exitOption == True:
            break
        else:
            loop = secMenu()

# ----------------#

# -    E n d    - #

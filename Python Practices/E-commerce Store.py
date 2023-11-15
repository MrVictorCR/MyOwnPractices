"""
    Welcome to my E-commerce Store, by Victor Mora Herrera
    I will be creating an E-commerce to sell clothes, make sure what you want! ;)

    I was specifically working on the return functions

    Also, as soon as I can I will add 'How do you want to pay?' , for example:
        Cash
        Debit Card
        Credit Card
    That will be added in future versions
"""


# - Vars from the items and that I need in the program -#
shoes = 60
sueter = 40
pants = 70
# ------------------------------------------------------#
total = 0
irequested = 0
condition = bool
# ------------------------------------------------------#

# - Main Menu: Displays the items that you can choose to buy -#


def menu():

    try:
        print("\nWhat do you want to buy?")
        irequested = int(input("1. Shoes\n" +
                               "2. Sueter\n" +
                               "3. Pants\n------- "))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return irequested

# ------------------------------------------------------------#

# - Adding Items Functions: Sum 'X Item' price to 'Total' -#


def addShoes(total):

    shoesColorList = ['Blue', 'Red', 'White']
    shoesSizeList = ['8/5', '9', '9/5']

    miniCondition = True

    while (miniCondition):

        try:
            print("\nWhat is the color that you want to buy?")
            shoesColor = int(input("1. Blue\n" +
                                   "2. Red\n" +
                                   "3. White\n------- "))
            if shoesColor == 1:
                shoesColor = shoesColorList[0]
                print('Color added\n')
            elif shoesColor == 2:
                shoesColor = shoesColorList[1]
                print('Color added\n')
            elif shoesColor == 3:
                shoesColor = shoesColorList[2]
                print('Color added\n')
            else:
                shoesColor = 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

            print("\nWhat size do you want?")
            shoesSize = int(input("1. 8/5\n" +
                                  "2. 9\n" +
                                  "3. 9/5\n------- "))
            if shoesSize == 1:
                shoesSize = shoesSizeList[0]
                print('Size added\n')
            elif shoesSize == 2:
                shoesSize = shoesSizeList[1]
                print('Size added\n')
            elif shoesSize == 3:
                shoesSize = shoesSizeList[2]
                print('Size added\n')
            else:
                shoesSize: 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

        finally:
            miniCondition = False
            total += shoes
            return shoesColor, shoesSize, total


def addSueter(total):

    sueterColorList = ['Blue', 'Red', 'Black']
    sueterSizeList = ['S', 'M', 'L', 'XL']

    miniCondition = True

    while (miniCondition):

        try:
            print("\nWhat is the color that you want to buy?")
            sueterColor = int(input("1. Blue\n" +
                                    "2. Red\n" +
                                    "3. Black\n------- "))
            if sueterColor == 1:
                sueterColor = sueterColorList[0]
                print('Color added\n')
            elif sueterColor == 2:
                sueterColor = sueterColorList[1]
                print('Color added\n')
            elif sueterColor == 3:
                sueterColor = sueterColorList[2]
                print('Color added\n')
            else:
                sueterColor = 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

            print("\nWhat is the color that you want to buy?")
            sueterSize = int(input("1. S\n" +
                                   "2. M\n" +
                                   "3. L\n" +
                                   "4. XL\n------- "))
            if sueterSize == 1:
                sueterSize = sueterSizeList[0]
                print('Size added\n')
            elif sueterSize == 2:
                sueterSize = sueterSizeList[1]
                print('Size added\n')
            elif sueterSize == 3:
                sueterSize = sueterSizeList[2]
                print('Size added\n')
            elif sueterSize == 4:
                sueterSize = sueterSizeList[3]
                print('Size added\n')
            else:
                sueterSize = 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")
        finally:
            miniCondition = False
            total += sueter
            return sueterColor, sueterSize, total


def addPants(total):

    pantsColorList = ['White', 'Black', 'Blue']
    pantsSizeList = [28, 30, 32, 34, 36, 38]

    miniCondition = True

    while (miniCondition):

        try:
            print("\nWhat is the color that you want to buy?")
            pantsColor = int(input("1. White\n" +
                                   "2. Black\n" +
                                   "3. Blue\n------- "))
            if pantsColor == 1:
                pantsColor = pantsColorList[0]
                print('Color added\n')
            elif pantsColor == 2:
                pantsColor = pantsColorList[1]
                print('Color added\n')
            elif pantsColor == 3:
                pantsColor = pantsColorList[2]
                print('Color added\n')
            else:
                pantsColor = 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

            print("\nWhat is the color that you want to buy?")
            pantsSize = int(input("1. 28\n" +
                                  "2. 30\n" +
                                  "3. 32\n" +
                                  "4. 34\n" +
                                  "5. 36\n" +
                                  "6. 38\n------- "))
            if pantsSize == 1:
                pantsSize = pantsSizeList[0]
                print('Size added\n')
            elif pantsSize == 2:
                pantsSize = pantsSizeList[1]
                print('Size added\n')
            elif pantsSize == 3:
                pantsSize = pantsSizeList[2]
                print('Size added\n')
            elif pantsSize == 4:
                pantsSize = pantsSizeList[3]
                print('Size added\n')
            elif pantsSize == 5:
                pantsSize = pantsSizeList[4]
                print('Size added\n')
            elif pantsSize == 6:
                pantsSize = pantsSizeList[5]
                print('Size added\n')
            else:
                pantsSize = 0
                raise ValueError(
                    "Error -> The Option you chosee doesn't exist \n")

        finally:
            miniCondition = False
            total += pants
            return pantsColor, pantsSize, total
    print("Pants added\n")


# ------------------------------------------------------------#

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to add another item" -#


def secMenu():
    print("\nDo you want something else?")
    c = int(input("1. Yes\n" +
                  "2. Get your total\n----------------- "))
    try:
        if c == 1:
            condition = True

        elif c == 2:
            print(f"\nYour total is: {total}$")
            descount = total * 0.15
            finalPrice = total - descount
            print(
                f"Due to the 15% discount in the store, the total payable will be: {finalPrice}$\n")
            print("\tThank you for using our services today! :)\n")

            condition = False

        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        condition = False

    finally:
        return condition

# ------------------------------------------------------------------------------------------------------------#

# - MAIN PROGRAM -#


print("\n\tWelcome to my E-commerce Store")
print(f"""
|---------------------|
|    What we Sell?    |
|  Shoes price: {shoes}$   |
|  Sueter price: {sueter}$  |
|  Pants price: {pants}$   |
|---------------------|""")

# - Loop Call -#
while (condition):

    # - Menu Call -#
    irequested = menu()

    try:
        if irequested == 1:
            shoesColor, shoesSize, total = addShoes(total)
            print(
                f"Shoes added: Shoes Color: {shoesColor}, Shoes Size: {shoesSize}, the total is: {total}")

        elif irequested == 2:
            sueterColor, sueterSize, total = addSueter(total)
            print(
                f"Sueter added: Sueter Color: {sueterColor}, Sueter Size: {sueterSize}, the total is: {total}")

        elif irequested == 3:
            pantsColor, pantsSize, total = addPants(total)
            print(
                f"Pants added: Pants Color: {pantsColor}, Pants Size: {pantsSize}, the total is: {total}")

        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        condition = secMenu()

# ----------------#

# -    E n d    -#

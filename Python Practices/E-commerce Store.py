"""
    Welcome to my E-commerce Store, by Victor Mora Herrera
    I will be creating an E-commerce to sell clothes, make sure what you want! ;)

    I was specifically working on the return functions

    Also, as soon as I can I will add some news in the clothes features, for example:
        Color
        Size, so on
    That will be added in future versions
"""


#- Vars from the items and that I need in the program -#
shoes = 60
sueter = 40
pants = 70
#------------------------------------------------------#
total = 0
irequested = 0
condition = bool
#------------------------------------------------------#

#- Main Menu: Displays the items that you can choose to buy -#

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
    
#------------------------------------------------------------#

#- Adding Items Functions: Sum 'X Item' price to 'Total' -#

def addShoes(total):
    total += shoes
    print("Shoes added\n")
    return total

def addSueter(total):
    total += sueter
    print("Sueter added\n")
    return total

def addPants(total):
    total += pants
    print("Pants added\n")
    return total

#------------------------------------------------------------#

#- "Secondary Menu ('secMenu'): this will help when you will be requested if you want to add another item" -#

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
            print(f"Due to the 15% discount in the store, the total payable will be: {finalPrice}$\n")
            print("\tThank you for using our services today! :)\n")
            
            condition = False

        else:
            raise ValueError ("Error -> The Option you chosee doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        condition = False

    finally:
        return condition

#------------------------------------------------------------------------------------------------------------#

#- MAIN PROGRAM -# 

print("\n\tWelcome to my E-commerce Store")
print(f"""
|---------------------|
|                     |
|   Shoes Price: {shoes}   |
|   Sueter Price: {sueter}  |
|   Pants Price: {pants}   |
|                     |
|---------------------|""")

#- Loop Call -#
while(condition):
    
    #- Menu Call -#
    irequested = menu()

    try: 
        if irequested == 1:
            total = addShoes(total)

        elif irequested == 2:
            total = addSueter(total)

        elif irequested == 3:
            total = addPants(total)
         
        else:
            raise ValueError ("Error -> The Option you chosee doesn't exist \n")
            
    
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
    
    finally:
        condition = secMenu()

#----------------#

#-    E n d    -#
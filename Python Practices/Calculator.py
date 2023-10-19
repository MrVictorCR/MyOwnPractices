


"""
Tengo un error con las excepciones, deberia de buscar como se lanzan y como las puedo atrapar, porque cuando lo hago parece que solo la lanzo pero no hay nada que lo atrape
"""

#- Vars that I need in the program -#

total = 0
num1 = 0
num2 = 0
z = bool
c = True

#-----------------------------------#

#- Main Menu: Displays the Calculator options -#

def menu():
    try:
        x = int(input(("""\t...:Menu:...
1. Sum
2. Subtract
3. Multiply
4. Divide
5. Exit
----------------- """)))
    
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
    
    finally:
        return x

#----------------------------------------------#
    
#- Number Request: 
"""
As this calculator has different option you will be requested for 2 different number many times,
so, with this function it will reduce the lines amount
"""
def numRequest(z, total):
    try:
        if z == True:
            num1 = total
            num2 = int(input("""
What would be the Next number?
--------- """))
        else:
            num1 = int(input("""
What would be the First number?
--------- """))
            num2 = int(input("""
What would be the Second number?
--------- """))
            
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return num1, num2
    
#---------------#


#- Adding Calculator Functions -#

def sum(num1, num2):
    total = num1 + num2
    print(f"\n\tSum Result: {total}\n")
    return total

def res(num1, num2):
    total = num1 - num2
    print(f"\n\Subtraction Result: {total}\n")
    return total

def mult(num1, num2):
    total = num1 * num2
    print(f"\n\tMultiplication Result: {total}\n")
    return total

def div(num1, num2):
    
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError ("Error -> It can't be divitions between '0'\n")
    else:
        total = num1 / num2
        print(f"\n\Division Result: {total}\n")

#------------------------#

#- "Secondary Menu ('secMenu'): In case that you want to use another function" -#

def secMenu(z):
    try:
        if z == False:
            z = False
            print("Make sure that the number that you want to divide is not '0'! :)\n")
        else:
            print("Do you want to do something else with this result?")
            c = int(input("1. Yes\n" +
                                "2. Exit\n------- "))

            if c == 1:
                z = True
                return c
            elif c == 2:
                print("\n\tThank you for using our services!\n" +
                    "\tEnjoy the rest of your day :) \n")
                z = False
            else:
                raise ValueError ("Error -> The Option you chose doesn't exist \n")
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
        print(f"Your result right now is: {total}\n")

    finally:
        return z
    
#------------------------------------------------------------------------------#

#- MAIN PROGRAM -# 

print("\n\tWelcome to SVS Calculator\n")

#- Loop Call -#
while(z):

    #- Menu Call -#
    x = menu()
    
    try:
        if x == 1: 
            num1, num2 = numRequest(z, total)
            total = sum(num1, num2)

        elif x == 2:
            num1, num2 = numRequest(z, total)
            total = res(num1, num2)

        elif x == 3:
            num1, num2 = numRequest(z, total)
            total = mult(num1, num2)

        elif x == 4:
            num1, num2 = numRequest(z, total)
            total = div(num1, num2)
        elif x == 5:
            print("\n\tThank you for using our services!\n" +
                    "\tEnjoy the rest of your day :) \n")
            c = False
        else:
            raise ValueError ("Error -> The Option you chose doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(total)
        print(UnexpectedNumber)
    except ZeroDivisionError as zde:
        print(zde)
        z = False

    finally:
        if c == False:
            break
        else:
            z = secMenu(z)

#----------------#

#-    E n d    -#
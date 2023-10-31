"""
    Welcome to my Drawing.py practice.
    In this case, I will be creating a program that it is going to console print a draw,
        This draw is going to be a sharp, will be create with '*' 
    
    So, in this case I'm going to request to enter the height and width from the drawing
    This would be with two For loops
        The first one is going to be for the height 
        And the second one is going to be for the width
    And I'm going to use the Print function with the 'end' parameter
"""
#- Vars that I need in the program -#

condition = True

#-----------------------------------#
def draw(height, width):
    for i in range(height):
        for x in range(width):
            print("* ",end="")
        print()
    print()

print("\t\n._.-Welcome to my Drawing program-._.")

while(condition):

    try:

        height = int(input("\nEnter the height value: "))
        width = int(input("\nEnter the width value: "))

        print()
        draw(height, width)
        condition = False

    except ValueError:
        print("\nError -> The values should be a digit/number")
"""
    Welcome to my School DataBase.py project.
    In this case I'm going to create a 'data base' that this would have everything regarding some students
    The information that I can save in this data base:
        ID
        First Name
        Last Name
        Phone Number
        Age
        Address
    
    What would be the options that I can do in this program?
        Add a new student
        Search a student
        Delete a student 
        See all the database

    I will be working with functions, conditionals, loops, so on.
"""

# - Vars that I need in the program -#

database = []
condition = bool
exitOption = False

# -----------------------------------#

# - Main Menu: Displays the options that the DataBase is going to have -#


def menu():

    try:
        x = int(input(f"""
1. To Add a New Student
2. To Search a Student
3. To Delete a Student
4. To See Every Student in the DB
5. Exit
--------------------------------- """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return x

# ----------------------------------------------------------------------#

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" -#


def secMenu():
    try:
        print("\nDo you want to do something else?")
        c = int(input("1. Yes\n" +
                      "2. Exit\n------- "))

        if c == 1:
            condition = True
        elif c == 2:
            print("\n\tThank you for using our services!\n\t" +
                  "Enjoy the rest of your day :) \n")
            condition = False
        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")
    except ValueError as UnexpectedOption:
        print(UnexpectedOption)
        condition = True

    finally:
        return condition

# --------------------------------------------------------------------------------------------------------------#

# - Adding DB Functions -#


def add_a_new_student(iD, firstName, lastName, phoneNumber, age, address):

    # I need to create a dict in order to add it to the 'DB', every time that I choose this option the dict will be reset it
    miniDict = {}

    miniDict['ID'] = iD
    miniDict['Fist Name'] = firstName
    miniDict['Last Name'] = lastName
    miniDict['Phone Number'] = phoneNumber
    miniDict['Age'] = age
    miniDict['Address'] = address

    database.append(miniDict)

    print('\nStudent added')

# What if I want to add a student with the same ID? - For that reason I created this for, to determine that the ID is not in 'database'


def id_already_exist(iD):

    if len(database) == 0:
        idAlreadyExist = False
    else:
        for i in database:
            if i['ID'] == iD:
                idAlreadyExist = True
            else:
                idAlreadyExist = False

    return idAlreadyExist


def search_a_student(iD):

    for i in database:
        if i['ID'] == iD:
            student = (
                f"Name: {i['Fist Name']}, Last Name: {i['Last Name']}, Phone Number: {i['Phone Number']}, Age: {i['Age']}, Address: {i['Address']}")
            return student
    return False


def delete_a_student(iD):

    for i in database:
        if i['ID'] == iD:
            database.remove(i)
            return True
        return False


def show_students():

    if len(database) == 0:
        print("\n\tWe didn't add a Student yet")
    else:
        print('\nShowing evey Student save in our DB')
        for i in database:
            print(
                f"\n\tName: {i['Fist Name']}, Last Name: {i['Last Name']}, Phone Number: {i['Phone Number']}, Age: {i['Age']}, Address: {i['Address']}")


# -----------------------#

# - MAIN PROGRAM -#

print('\n\t-__Welcome to SVS Students DataBase__-')

while (condition):

    option = menu()

    try:
        if option == 1:
            iD = input('\nWhat is the Student ID?\n' +
                       '-------------------- ')
            if id_already_exist(iD):
                print('There is a Student already added with that ID')
            else:
                firstName = input('\nWhat is the Student First Name?\n' +
                                  '-------------------- ')
                lastName = input('\nWhat is the Student Last Name?\n' +
                                 '-------------------- ')
                phoneNumber = input('\nWhat is the Student Phone Number?\n' +
                                    '-------------------- ')
                age = input('\nWhat is the Student Age?\n' +
                            '-------------------- ')
                address = input('\nWhat is the Student Address?\n' +
                                '-------------------- ')
                add_a_new_student(iD, firstName, lastName,
                                  phoneNumber, age, address)

        elif option == 2:
            iD = input('\nWhat is the Student ID?\n' +
                       '-------------------- ')
            if search_a_student(iD) == False:
                print("\nThe Student doesn't exist")
            else:
                print('\nStudent Found\n')
                print(search_a_student(iD))

        elif option == 3:
            iD = input('\nWhat is the Student ID?\n' +
                       '-------------------- ')
            if delete_a_student(iD):
                print('\nStudent Removed')
            else:
                print("\nThe Student doesn't exist")

        elif option == 4:
            show_students()

        elif option == 5:
            print("\n\tThank you for using our services!\n" +
                  "\tEnjoy the rest of your day :) \n")
            exitOption = True

        else:
            raise ValueError("\nError -> The Option you chosee doesn't exist")

    except ValueError as UnexpectedOption:
        print(UnexpectedOption)

    finally:
        if exitOption == True:
            break

        else:
            condition = secMenu()

# ----------------#

# -    E n d    -#

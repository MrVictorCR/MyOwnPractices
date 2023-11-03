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

    I will be working with classes, conditionals, loops, so on.
"""

# Guardar la info de esta manera, un dict en el que la key será el ID y el value será de ser posible una list, si no es el caso ya veremos como lo hacemos


#- Vars that I need in the program -#

database = []
condition = bool

iD = ''
firstName = ''
lastName = ''
phoneNumber = ''
age = ''
address = ''


#-----------------------------------#

#- Main Menu: Displays the options that the DataBase is going to have -#

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

#----------------------------------------------------------------------#

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

#- Adding DB Functions -#

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

def search_a_student(iD):

    for i in database:
        if i['ID'] == iD:
            student = (f"Name: {i['Fist Name']}, Last Name: {i['Last Name']}, Phone Number: {i['Phone Number']}, Age: {i['Age']}, Address: {i['Address']}")
            return student
        return False

def delete_a_student():

    for i in database:
        if i['ID'] == iD:
            database.remove(i)
            return True
        return False

def show_students():

    if i <= len(database):
        for i in database:
            print(f"Name: {i['Fist Name']}, Last Name: {i['Last Name']}, Phone Number: {i['Phone Number']}, Age: {i['Age']}, Address: {i['Address']}")
    else:
        print("We didn't add a Student yet")

#-----------------------#

#- MAIN PROGRAM -# 

print('\n\tWelcome to SVS Students DataBase')

# To-do 
# while(condition):



#----------------#

#-    E n d    -#
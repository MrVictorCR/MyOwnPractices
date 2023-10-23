"""
    Welcome to my Phonebook.py
        I will be creating a program that it will represent a Phonebook
        In this case it will have different options, so, depending on what you need you will be able to choose that option
        The options will be the following:
            1. New Contact
            2. Delete Contact
            3. View Contacts
            4. Exit

        I will be practicing with:
            List, Dic, Exceptions
"""

#- Vars from the items and that I need in the program -#

agenda = {}
opt = 0
condition = bool
c = True

#------------------------------------------------------#

#- Main Menu: Displays the PhoneBook Options -#

def menu():

    try: 

        print("\nWhat do you want to do?")
        opt = int(input("1. Add New Contact\n" +
                                "2. Delete Contact\n" +
                                "3. View Contacts\n" +
                                "4. Exit\n------------- "))
        
    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)
    
    finally:
        return opt

#---------------------------------------------#

#- Adding PhoneBook Options -#

def addNC(name, phone):

    if name not in agenda:
            agenda[name] = phone
            print("Contact added")
    else: 
        print("The contact already Exist\n")

def delContact(name):

    if name in agenda:
        del(agenda[name])
        print("Contact Deleted\n")
    else:
        print("The Contact Name doesn't Exist\n")

def vContact():

    print("\n\t#-- PhoneBook --#\n")

    for key,value in agenda.items():
        print(f"Name: {key}, Phone #: {value}") 

#----------------------------#

#- "Secondary Menu ('secMenu'): this will help when you will be requested if you want to do another option" -#

def secMenu():
    print("\nDo you want something else?")
    c = int(input("1. Yes\n" +
                          "2. Exit\n------ "))
    try:

        if c == 1:
            condition = True
        
        elif c == 2:

            print("\nThank you for using our services!\n\t" +
                  "Enjoy the rest of your day :) \n\t")
            
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

print("\n\tWelcome to my PhoneBook")

#- Loop Call -#
while(condition):

    #- Menu Call -#
    opt = menu()

    try:

        if opt == 1:
            name = input("Contact Name: ")
            phone = input("Contact Phone Number: ")
            addNC(name, phone)
        
        if opt == 2:
            name = input("Contact Name: ")
            delContact(name)
        
        if opt == 3:
            vContact()
        
        if opt == 4:
            print("\n\tThank you for using our services!\n" +
                    "\tEnjoy the rest of your day :) \n")
            c = False
        
        else:
            raise ValueError ("Error -> The Option you chose doesn't exist \n")

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:

        if c == False:
            break
        else:
            condition = secMenu()

#----------------#

#-    E n d    -#
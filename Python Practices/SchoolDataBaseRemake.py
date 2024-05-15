

"""
    Creating a new Remake for the School DB, right here I will be creating a Person class to identify if it is a student or a teacher
    Using the same info as previously program but, trying to implement some funtions from a Class.

"""

# - Vars that I need in the program -#

preStudentDB = []
studentDB = []
teacherDB = []
condition = bool
exitOption = False

# -----------------------------------#

# - Trying to implement a Class - #


class Person():
    def __init__(self, iD, name, lastName, position):
        self.iD = iD
        self.name = name
        self.lastName = lastName
        self.position = position

    # - Create Person - #

    def savePerson(self):

        personDict = {}
        personDict['ID'] = self.iD
        personDict['Name'] = self.name
        personDict['Last Name'] = self.lastName

        if self.position == 1:
            self.position = 'Student'
            personDict['Position'] = self.position
            preStudentDB.append(personDict)
            return 0
        elif self.position == 2:
            self.position = 'Teacher'
            personDict['Position'] = self.position
            teacherDB.append(personDict)
            return 0
        else:
            print('Incorrect Option')
            return 1


class Student(Person):

    def __init__(self, iD, name, lastName, position):
        super().__init__(iD, name, lastName, position)

    # - Create Student - # Edit Student Option

    def saveStudent(self, age, phoneNumber, address):

        for i in preStudentDB:
            if i['ID'] == self.iD:
                studentName = i['Name']
                studentLastName = i['Last Name']

                studentDict = {}
                studentDict['ID'] = self.iD
                studentDict['Name'] = studentName
                studentDict['Last Name'] = studentLastName
                studentDict['Age'] = age
                studentDict['Phone Number'] = phoneNumber
                studentDict['Address'] = address
                studentDB.append(studentDict)

                return 0

        return 1

    # - Search Student - # Search Student Option

    def searchStudent(iD):
        if len(studentDB) == 0:
            print('There is not student added yet')
        else:
            for i in studentDB:
                if i['ID'] == iD:
                    studentExist = True
                    student = (f"""
Student ID: {i['ID']}
Student Name: {i['Name']} {i['Last Name']}
Student Age: {i['Age']}
Student Phone#: {i['Phone Number']}
Student Address: {i['Address']}
""")
                    return studentExist, student
                else:
                    studentExist = False

# ---------------------------------#

# - Menus - #

# - Main Menu: Displays MAIN DB Options - #


def menu():

    try:
        option = int(input(f"""
1. To Add a New Person
2. Modify a Person
3. To View a Database
4. Exit
---------------------------- """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return option
# --------------------------------------- #

# - Student Menu / Functions - #


def studentMenuConditional():
    option = int(input(f"""
Do you want to add the Student Information right now?

1. Yes
2. No

------- """))
    return option


def addStudentInformation():
    print('\n\tCreating a New Student')
    sAge = input("\nWhat is Student's Age?\n-------------- ")
    sPhoneNumber = input("\nWhat is Student's Phone Number?\n-------------- ")
    sAddress = input("\nWhat is Student's Address?\n-------------- ")
    return sAge, sPhoneNumber, sAddress
# ---------------- #

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" - #


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

# -------------------------------------------------------------------------------------------------------------- #

# --------- #

# - Verification's Function - #


def idAlreadyExist(iD):

    preStudent = ''
    teacher = ''

    if (len(preStudentDB) == 0) and (len(teacherDB) == 0):
        idCondition = 0
        return preStudent, teacher, idCondition

    else:
        for i in preStudentDB:
            if iD == i['ID']:
                preStudent = (
                    f"ID: {i['ID']}, Name: {i['Name']}, Last Name: {i['Last Name']}, Position: {i['Position']}")
                idCondition = 1
                return preStudent, teacher, idCondition
            else:
                idCondition = 0

        for i in teacherDB:
            if iD == i['ID']:
                teacher = (
                    f"ID: {i['ID']}, Name: {i['Name']}, Last Name: {i['Last Name']}, Position: {i['Position']}")
                idCondition = 1
                return preStudent, teacher, idCondition
            else:
                idCondition = 0

        return preStudent, teacher, idCondition


def assingNewValues(menuOption, iD, name, lastName, position, age, phoneNumber, address):

    newID = iD
    newFirstName = name
    newLastName = lastName
    newPosition = position
    newAge = age
    newPhoneNumber = phoneNumber
    newAddrees = address
    newDict = {}

    if menuOption == 0:
        for i in preStudentDB:
            if newID == i['ID']:
                preStudentDB.remove(i)

        editNewValueOption = int(input("""
What do you want to edit?

1 -> ID
2 -> Fist Name
3 -> Last Name
5 -> Age
6 -> Phone Number
7 -> Address

------------------ """))

    elif menuOption == 1:
        editNewValueOption = int(input("""
What do you want to edit?

1 -> ID
2 -> Fist Name
3 -> Last Name
4 -> Position

------------------ """))

    if editNewValueOption == 1:
        newID = int(
            input('What was the right ID?\n--------------- '))
        preStudent, teacher, idCondition = idAlreadyExist(newID)
        if idCondition == 1:
            print(f"""
There is a person already with that ID number
{preStudent} 
{teacher}""")
            newStudent = 1
            return 1, newDict, newStudent
    elif editNewValueOption == 2:
        newFirstName = input(
            'What was the right First Name?\n--------------- ')
    elif editNewValueOption == 3:
        newLastName = input(
            'What was the right Last Name?\n--------------- ')
    elif editNewValueOption == 5:
        newAge = int(
            input('How old is he/she?\n--------------- '))
    elif editNewValueOption == 6:
        newPhoneNumber = input(
            'What was the right Phone Number?\n--------------- ')
    elif editNewValueOption == 7:
        newAddrees = input(
            'What was the right Address?\n--------------- ')

    elif editNewValueOption == 4:
        newPosition = int(input("""
What is the right Position?
                    
1 -> Student
2 -> Teacher
                            
--------------- """))
        if newPosition == 1:
            newPosition = 'Student'
        elif newPosition == 2:
            newPosition = 'Teacher'
        else:
            print('Incorrect Option')

    else:
        print('Incorrect Option')
        return 1

    if menuOption == 0:
        newDict['ID'] = newID
        newDict['Name'] = newFirstName
        newDict['Last Name'] = newLastName
        newDict['Position'] = 'Student'
        preStudentDB.append(newDict)
        newDict.pop('Position')
        newDict['Age'] = newAge
        newDict['Phone Number'] = newPhoneNumber
        newDict['Address'] = newAddrees
        newStudent = 1

    elif menuOption == 1:

        if newPosition == 'Student':
            conditional = studentMenuConditional()
            if conditional == 1:
                newDict['ID'] = newID
                newDict['Name'] = newFirstName
                newDict['Last Name'] = newLastName
                newDict['Position'] = newPosition
                preStudentDB.append(newDict)
                newStudent = Student(
                    newID, newFirstName, newLastName, newPosition)
                newAge, newPhoneNumber, newAddress = addStudentInformation()
                newStudent = newStudent.saveStudent(
                    newAge, newPhoneNumber, newAddress)
                if newStudent == 0:
                    print('\nNew Student added')
                    return 0, newDict, newStudent
                else:
                    print('\nStudent was not created')
            elif conditional == 2:
                newStudent = 1
                print('\nFinishing process')
            else:
                print('\nIncorrect Option')
        else:
            newStudent = 1

        newDict['ID'] = newID
        newDict['Name'] = newFirstName
        newDict['Last Name'] = newLastName
        newDict['Position'] = newPosition

    return 0, newDict, newStudent


def changeDataBase(condition, editOption, iD):
    age = int
    phoneNumber = ''
    address = ''
    position = ''

    if editOption == 1:

        if len(teacherDB) == 0:
            return 1
        else:
            for i in teacherDB:
                if iD == i['ID']:
                    if condition == 2:
                        teacherDB.remove(i)
                        return 0
                    elif condition == 1:
                        name, lastName, position = i['Name'], i['Last Name'], i['Position']
                        teacherDB.remove(i)
                        menuOption = 1
                        assingValuesCondition, newPerson, newStudent = assingNewValues(
                            menuOption, iD, name, lastName, position, age, phoneNumber, address)
                        if newPerson['Position'] == 'Teacher':
                            teacherDB.append(newPerson)
                        elif newPerson['Position'] == 'Student':
                            if newStudent == 1:
                                preStudentDB.append(newPerson)
                        return assingValuesCondition
                    else:
                        print('\n\tIncorrect Option')
                        return 1
                else:
                    print('\n\tNo Teacher with that ID')
                    return 1
    elif editOption == 2:

        if len(studentDB) == 0:

            for i in preStudentDB:
                if iD == i['ID']:
                    if condition == 2:
                        preStudentDB.remove(i)
                        return 0
                    elif condition == 1:
                        name, lastName, position = i['Name'], i['Last Name'], i['Position']
                        preStudentDB.remove(i)
                        menuOption = 1
                        assingValuesCondition, newPerson, newStudent = assingNewValues(
                            menuOption, iD, name, lastName, position, age, phoneNumber, address)
                        if newPerson['Position'] == 'Teacher':
                            teacherDB.append(newPerson)
                        elif newPerson['Position'] == 'Student':
                            if newStudent == 1:
                                preStudentDB.append(newPerson)
                        return assingValuesCondition
                    else:
                        print('\n\tIncorrect Option')
                        return 1
                else:
                    print('\n\tNo Student with that ID')
                    return 1
        else:

            for i in studentDB:
                if iD == i['ID']:
                    if condition == 2:
                        studentDB.remove(i)
                        for i in preStudentDB:
                            if i == i['ID']:
                                preStudentDB.remove(i)
                        return 0
                    elif condition == 1:
                        name, lastName, age, phoneNumber, address = i['Name'], i['Last Name'], i['Age'], i['Phone Number'], [
                            'Address']
                        studentDB.remove(i)
                        menuOption = 0
                        assingValuesCondition, newPerson, newStudent = assingNewValues(
                            menuOption, iD, name, lastName, position, age, phoneNumber, address)
                        studentDB.append(newPerson)
                        return assingValuesCondition
                    else:
                        print('\n\tIncorrect Option')
                        return 1
                else:
                    studentNotFounded = True

            if studentNotFounded == True:
                for i in preStudentDB:
                    if iD == i['ID']:
                        if condition == 2:
                            preStudentDB.remove(i)
                            return 0
                        elif condition == 1:
                            name, lastName, position = i['Name'], i['Last Name'], i['Position']
                            preStudentDB.remove(i)
                            menuOption = 1
                            assingValuesCondition, newPerson, newStudent = assingNewValues(
                                menuOption, iD, name, lastName, position, age, phoneNumber, address)
                            if newStudent == 1:
                                preStudentDB.append(newPerson)
                            return assingValuesCondition

                        else:
                            print('\n\tIncorrect Option')
                            return 1
                return 1


def showDB(condition):
    if condition == 1:
        if len(preStudentDB) == 0:
            return 1
        else:
            if len(studentDB) == 0:
                for i in preStudentDB:
                    print(
                        f"ID: {i['ID']}, Name: {i['Name']}, Last Name: {i['Last Name']}")
            else:
                print('\nShowing every Student in our Database')
                for i in preStudentDB:
                    siD = i['ID']
                    sName = i['Name']
                    sLastName = i['Last Name']
                    subCondition = False
                    for i in studentDB:
                        if siD == i['ID']:
                            print(
                                f"\n\tID: {i['ID']}, Name: {i['Name']}, Last Name: {i['Last Name']}, Phone Number: {i['Phone Number']}, Age: {i['Age']}, Address: {i['Address']}")
                            subCondition = True

                    if subCondition == False:
                        print(
                            f"\n\tID: {siD}, Name: {sName}, Last Name: {sLastName}")

    elif condition == 2:
        if len(teacherDB) == 0:
            return 1
        else:
            print('\nShowing every Teacher in our Database')
            for i in teacherDB:
                print(
                    f"\nID: {siD}, Name: {sName}, Last Name: {sLastName}")
# -------------------------- #


# - MAIN PROGRAM -#

# TRY TO SEE IF DELETE OPTION WORK AND THEN TRY THE SHOW OPTION
print('\n\t-__Welcome to SVS School DataBase__-')

while (condition):

    option = menu()
    try:
        if option == 1:
            print('\n\tCreating a New Person')
            iD = int(input("\nWhat is New Person's ID?\n-------------- "))
            preStudent, teacher, idCondition = idAlreadyExist(iD)
            if idCondition == 0:
                pName = input('\nWhat is your First Name?\n-------------- ')
                pLastName = input('\nWhat is your Last Name?\n-------------- ')
                position = int(input(
                    f"""
What is {pName}'s position?

If {pName} is a Student type -> 1
If {pName} is a Teacher type -> 2

---------------------------- """))
                print(f"\n\tUploading {pName} in our DB")

                newPerson = Person(iD, pName, pLastName, position)
                newPersonCreated = newPerson.savePerson()
                if newPersonCreated == 0:
                    print(f"\n{pName} profile was created succesfully")
                    if position == 1:
                        studentConditional = bool
                        while (studentConditional):
                            studentMenuOption = studentMenuConditional()

                            if studentMenuOption == 1:
                                newStudent = Student(
                                    newPerson.iD, newPerson.name, newPerson.lastName, newPerson.position)
                                sAge, sPhoneNumber, sAddress = addStudentInformation()
                                newStudent = newStudent.saveStudent(
                                    sAge, sPhoneNumber, sAddress)
                                if newStudent == 0:
                                    print('\nNew Student added')
                                    studentConditional = False
                                else:
                                    print('Student was not created')
                                    studentConditional = False
                            elif studentMenuOption == 2:
                                break
                            else:
                                print('Incorrect Option')
                elif newPersonCreated == 1:
                    print(
                        f"Unable to create {pName}, Position Option Incorrect")
            else:
                print(f"""
There is a person already with that ID number
{preStudent} 
{teacher}""")
        elif option == 2:
            print('\n\tExecuting Edit Option')
            condition = int(input("""
What do you want to do?
                              
1. Edit a Profile
2. Delete a Profile
                              
----------------------- """))
            editOption = int(input("""
To who do you want to do the change?
                                   
1. Teacher 
2. Student
    
-------------- """))
            iD = int(input("\nWhat is the Person's ID?\n--------------- "))
            changeCompletedCondition = changeDataBase(
                condition, editOption, iD)
            if changeCompletedCondition == 0:
                print('\nThe change to the ID was completed properly')
            else:
                print('\nThe change to the ID was not completed properly')

        elif option == 3:
            condition = int(input("""
What Database would you like to see?
                              
1. Student Database
2. Teacher Database
        
----------------------- """))
            showDBCondition = showDB(condition)
            if showDBCondition == 1:
                print('\nNot values founded')

        elif option == 4:
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

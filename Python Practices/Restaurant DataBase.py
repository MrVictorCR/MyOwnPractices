"""
    Welcome to my Restaurant project.
    In this case I'm going to create a 'data base' that it will contain information regarding some restaurants
    The information that I can save in this data base:
        
        Firstable will be a Database from a Restaurant:
            ID
            Restaurant Name
            Address
            Phone Number
        Next one will be a Database from Dishes:
            ID
            Dish Name
            Price
            Amount
        And finally, I will connect dishes to X restaurant, this will have:
            Restaurant
            Dish
        
    
    What would be the options that I can do in this program?:
        Add a new Restaurant
        View the Restaurants
        Delete a Restaurant

        Add a Dish
        View the Dishes
        Delete the Dishes

        Add a Dish to a Restaurant

    I will be working functions, conditionals, loops, so on.
"""

# - Vars that I need in the program -#

restaurantDatabase = []
dishDatabase = []
dishXRestaurant = []
condition = bool
exitOption = False
saveDishCondition = bool

# -----------------------------------#

# - Main Menu: Displays the options that the DataBase is going to have -#


def menu():

    try:
        option = int(input(f"""
1. To Add a New Restaurant
2. To View the Restaurants
3. To Delete a Restaurant
4. To Add a Dish
5. To View the Dishes
6. To Delete a Dish
7. To Add a Dish to a Restaurant
8. View all Dishes connected to a Restaurant
9. Exit 
--------------------------------- """))

    except ValueError as UnexpectedNumber:
        print(UnexpectedNumber)

    finally:
        return option

# ----------------------------------------------------------------------#

# - "Secondary Menu ('secMenu'): this will help when you will be requested if you want to use another function" -#


def secMenu():
    try:
        print("\nDo you want to do something else?")
        opt = int(input("1. Yes\n" +
                        "2. Exit\n------- "))

        if opt == 1:
            condition = True
        elif opt == 2:
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


def add_a_restaurant(restaurantID, restaurantName, address, phoneNumber):
    # I need to create a dict in order to add it to the 'DB', every time that I choose this option the dict will be reset it
    miniRestaurantDict = {}

    miniRestaurantDict['ID'] = restaurantID
    miniRestaurantDict['Restaurant Name'] = restaurantName
    miniRestaurantDict['Address'] = address
    miniRestaurantDict['Phone Number'] = phoneNumber

    restaurantDatabase.append(miniRestaurantDict)

    print('\nRestaurant added')


def rest_id_already_exist(restaurantID):

    if len(restaurantDatabase) == 0:
        idAlreadyExist = False
    else:
        for i in restaurantDatabase:
            if i['ID'] == restaurantID:
                idAlreadyExist = True
            else:
                idAlreadyExist = False

    return idAlreadyExist


def view_restuarants():
    if len(restaurantDatabase) == 0:
        print("\n\tWe didn't add a Restaurant yet")
    else:
        print('\nShowing evey Restaurant save in our DB')
        for i in restaurantDatabase:
            print(
                f"\n\tRestaurant: {i['Restaurant Name']}, Phone Number: {i['Phone Number']}, Address: {i['Address']}")


def delete_restuarant(restaurantID):
    for i in restaurantDatabase:
        if i['ID'] == restaurantID:
            restaurantDatabase.remove(i)
            return True
        return False


def add_a_dish(dishID, dishName, price, quantity):
    miniDishDict = {}

    miniDishDict['ID'] = dishID
    miniDishDict['Dish Name'] = dishName
    miniDishDict['Price'] = price
    miniDishDict['Quantity'] = quantity

    dishDatabase.append(miniDishDict)

    print('\nDish added')


def dish_id_already_exist(dishID):

    if len(dishDatabase) == 0:
        idAlreadyExist = False
    else:
        for i in dishDatabase:
            if i['ID'] == dishID:
                idAlreadyExist = True
            else:
                idAlreadyExist = False

    return idAlreadyExist


def view_dishes():
    if len(dishDatabase) == 0:
        print("\n\tWe didn't add a Dish yet")
    else:
        print('\nShowing every Dish save in our DB')
        for i in dishDatabase:
            print(
                f"\n\tDish: {i['Dish Name']}, Price: {i['Price']}, Quantity: {i['Quantity']}")


def delete_dish(dishID):
    for i in dishDatabase:
        if i['ID'] == dishID:
            dishDatabase.remove(i)
            return True
        return False


def add_another_dish():
    try:
        print("\nDo you want to do add another dish?")
        opt = int(input("1. Yes\n" +
                        "2. Exit\n------- "))

        if opt == 1:
            saveDishCondition = True
        elif opt == 2:
            saveDishCondition = False
        else:
            raise ValueError("Error -> The Option you chosee doesn't exist \n")
    except ValueError as UnexpectedOption:
        print(UnexpectedOption)
        saveDishCondition = True

    finally:
        return saveDishCondition


def get_info_from_resturant():
    for i in restaurantDatabase:
        print(
            f"ID: {i['ID']}, Restaurant Name: {i['Restaurant Name']}")
    restaurantOption = int(input('What is the Restaurant ID that you want to choose?\n' +
                                 '-----------------------------------  '))
    for i in restaurantDatabase:
        if i['ID'] == restaurantOption:
            rest = (f"Restaurant: {i['Restaurant Name']}")

    return rest


def get_info_from_dish():
    for i in dishDatabase:
        print(
            f"ID: {i['ID']}, Dish Name: {i['Dish Name']}")
    dishOption = int(input('What is the Dish ID that you want to choose?\n' +
                           '-----------------------------------  '))

    for i in dishDatabase:
        if i['ID'] == dishID:
            dish = (f"Dish: {i['Dish Name']}")

    return dish, dishOption


def add_a_dish_to_a_restuarant(dishID, rest, dish):
    miniDishxRestaurantDict = {}

    miniDishxRestaurantDict['ID'] = dishID
    miniDishxRestaurantDict['Restaurant'] = rest
    miniDishxRestaurantDict['Dish'] = dish

    dishXRestaurant.append(miniDishxRestaurantDict)

    print('\nDish added to the Restaurant')


def view_all_dishes_connected_to_a_restaurant():
    x = 0
    if len(dishXRestaurant) == 0:
        print('There is not a Dish linked to a Restaurant yet')
    else:
        for i in dishXRestaurant:
            if i['ID'] == x:
                print()
            elif i['ID'] != x:
                print(f"ID: {i['ID']}, {i['Restaurant']}")
                x = i['ID']
    try:
        restOption = int(input('What is the ID from the Restaurant that you want to see their Dishes added?:\n' +
                               '------------------------- '))
        for i in dishXRestaurant:
            if i['ID'] == restOption:
                print(f"{i['Dish']}")
    except ValueError as UnexpectedOption:
        print(UnexpectedOption)

# -----------------------#

# - MAIN PROGRAM -#


print('\n\t-__Welcome to SVS Restaurants DataBase__-')

while (condition):

    option = menu()

    try:
        if option == 1:
            restaurantID = int(input('\nWhat is the Restaurant ID?\n' +
                                     '-------------------- '))
            if rest_id_already_exist(restaurantID):
                print('There is a Restaurant already added with that ID')
            else:
                restaurantName = input('\nWhat is the Restaurant Name?\n' +
                                       '-------------------- ')
                address = input('\nWhat is the Restaurant Address?\n' +
                                '-------------------- ')
                phoneNumber = input('\nWhat is the Restaurant Phone Number?\n' +
                                    '-------------------- ')
                add_a_restaurant(restaurantID, restaurantName,
                                 phoneNumber, address)

        elif option == 2:
            view_restuarants()

        elif option == 3:
            restaurantID = int(input('\nWhat is the Restaurant ID?\n' +
                                     '-------------------- '))
            if delete_restuarant(restaurantID):
                print('\nRestaurant Removed')
            else:
                print("\nThe Restaurant doesn't exist")

        elif option == 4:
            dishID = int(input('\nWhat is the Dish ID?\n' +
                               '-------------------- '))
            if dish_id_already_exist(dishID):
                print('There is a Dish already added with that ID')
            else:
                dishName = input('\nWhat is the Dish Name?\n' +
                                 '-------------------- ')
                price = input('\nWhat is the Dish Price?\n' +
                              '-------------------- ')
                quantity = input('\nHow many Dishes do you Have?\n' +
                                 '-------------------- ')
                add_a_dish(dishID, dishName, price, quantity)

        elif option == 5:
            view_dishes()

        elif option == 6:
            dishID = int(input('\nWhat is the Dish ID?\n' +
                               '-------------------- '))
            if delete_dish(dishID):
                print('\nRestaurant Removed')
            else:
                print("\nThe Dish doesn't exist")

        elif option == 7:
            if len(restaurantDatabase) == 0:
                print('There is not a Restaurant added yet')
            else:
                if len(dishDatabase) == 0:
                    print('We cannot add a Dish, because there is not a Dish added yet')
                else:
                    rest = get_info_from_resturant()
                    # A loop to save the dishes the amount that the user wants
                    while (saveDishCondition):
                        dish, dishOption = get_info_from_dish()
                        add_a_dish_to_a_restuarant(dishOption, rest, dish)
                        saveDishCondition = add_another_dish()

        elif option == 8:
            view_all_dishes_connected_to_a_restaurant()
        elif option == 9:
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

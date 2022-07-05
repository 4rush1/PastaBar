def get_integer(l):
    my_integer = int(input(l))
    return my_integer

def get_string(l):
    my_string = input(l)
    return my_string

def print_list(l):
    for i in range(0, len(l)):
        output = "{:10} {:10}".format(l[i][0], l[i][1])
        print(output)

def print_with_price(l):
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {:<30} ${:.2f}".format(i, l[i][0], l[i][1]))

def print_with_indexes(l):
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {}".format(i, l[i][0]))

def review_order(l):
    for i in range(0, len(l)):
        print("-" * 50)
        output = "You have ordered {} {} for ${:.2f}".format(l[i][0], l[i][1], l[i][2])
        print(output)

def print_pasta(m):
    print_list(m)
    print("-" * 50)

def order(m):
    order_loop = True
    while order_loop is True:
        print_with_price(m)
        order_list = []
        dish = get_integer("Enter the number of the dish you would like to order ---> ")
        name = m[dish][0]
        amount = get_integer("How many would you like ---> ")
        price = m[dish][1]
        total_price = price * amount
        temp_list = [amount, name, total_price]
        order_list.append(temp_list)
        review_order(order_list)
        print("-" * 50)
        if get_confirmation() is False:
            return None
        # do you want to order again
        # if not return None

def get_confirmation(m = "Do you want to continue on this menu (C) or return back the main menu (R)"):
    response = input(m)
    while response not in ["C", "R"]:
        print("This is not a recognised entry")
        return False
    if response == "C":
        return True
    else:
        return False

def get_order_menu():
    pasta_menu = [
        ["Linguine Gamberi", 23],
        ["Fusilli Pesto", 19],
        ["Conchilglie alla Bolognese", 22],
        ["Rigatoni alla Caponata", 21],
        ["Fettuccine Carbonara", 20],
        ["Spaghetti Pomodoro", 16],
        ["Pappardelle Ricci D’Angello", 26],
        ["Raviolo di Salsiccia", 22],
        ["Ravioli di Ricotta", 20]
    ]

    vegan_menu = [
        ["Vegan Pomodoro", 16],
        ["Vegan Gamberi", 23],
        ["Vegan Caponata", 21],
        ["Vegan Pesto", 19]
    ]

    antipasto_menu = [
        ["Garlic and Rosemary Roll", 3],
        ["Marinated Olives", 10],
        ["Giardiniera", 6],
        ["Greens", 12],
        ["Rocket", 12]
    ]

    desserts_menu = [
        ["Panna Cotta", 10],
        ["Torta Cioccolato", 10]
    ]

    food_menu = [
        ["Pasta"],
        ["Vegan"],
        ["Antipasto"],
        ["Desserts"],
    ]

    print_with_indexes(food_menu)
    print("-" * 50)

    # CHOOSE WHICH MENU YOU WANT
    choose_menu = get_integer("Select the number of the menu you would like to print ---> ")
    if choose_menu == 0:
        print("-" * 50)
        return pasta_menu
    elif choose_menu == 1:
        print("-" * 50)
        return vegan_menu
    elif choose_menu == 2:
        print("-" * 50)
        return antipasto_menu
    elif choose_menu == 3:
        print("-" * 50)
        return desserts_menu
    else:
        print("-" * 25)
        print("Invalid entry, try again")
        print("-" * 50)

def main():
    menu_list = [
        ["P", "Print menu"],
        ["O", "Order"],
        ["Q", "Quit"]
    ]

#  MENU LOOP
    menu_loop = True
    while menu_loop is True:
        print("-" * 50)
        print_list(menu_list)
        print("-" * 50)
        # CHOOSE MENU OPTION : PRINT OR QUIT
        user_choice = get_string("Please select an option from the menu above --> ")
        print("-" * 50)
        # CHOICE P
        if user_choice == "P":
            menu = get_order_menu()
            print_with_price(menu)
        # CHOICE O
        elif user_choice == "O":
            menu = get_order_menu()
            order(menu)
        # CHOICE Q
        elif user_choice == "Q":
            menu_loop = False
            print("Thank you for your time")

        else:
            print("-" * 25)
            print("Invalid entry, try again")
            print("-" * 50)


if __name__ == "__main__":
    main()



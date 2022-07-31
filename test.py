def get_integer(l):
    my_integer = int(input(l))
    return my_integer

def get_string(l):
    try:
        my_string = input(l)
        return my_string.upper()
    except:
        print("sorry invalid entry, try again")

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

def print_order_with_indexes(l):
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {} {}".format(i, l[i][0], l[i][1]))

#def review_total_order_grand(o_list):
    #for i in range(0, len(o_list)):
    #    grand_total = sum(o_list[i][2])
   #     print("your total bill is {:.2f}".format(grand_total))

def review_total_order(l):
    for i in range(0, len(l)):

        output = "You have ordered {} {} for ${:.2f}".format(l[i][0], l[i][1], l[i][2])
        print(output)

def review_order(l):
    output = "You have ordered {} {} for ${:.2f}".format(l[0], l[1], l[2])
    print(output)

def print_pasta(m):
    print_list(m)

def get_confirmation(m = "Do you want to continue on this menu (C) or return back the main menu (R)"):
    # do you want to order again
    # if not return None
    response = input(m)
    print("_" * 50)
    while response not in ["C", "R"]:
        print("This is not a recognised entry")
        return False
    if response == "C":
        return True
    else:
        return False

def order(m, o_list):
    order_loop = True
    while order_loop is True:
        if get_confirmation() is False:
            review_total_order(o_list)
            return None
        print_with_price(m)
        print("_" * 50)
        dish = get_integer("Enter the number of the dish you would like to order ---> ")
        name = m[dish][0]
        amount = get_integer("How many would you like ---> ")
        price = m[dish][1]
        total_price = price * amount
        temp_list = [amount, name, total_price]
        o_list.append(temp_list)
        print("_" * 50)
        review_order(temp_list)
        print("_" * 50)

def edit_order(o_list):
    edit_order_loop = True
    while edit_order_loop is True:
        print_order_with_indexes(o_list)
        print("_" * 50)
        my_index = get_integer("Please enter the number of the dish you would like to edit / remove")
        name = o_list[my_index][1]
        new_amount = get_integer("How many {} do you want now? If you would like to remove this dish, please enter 0".format(o_list[my_index][1]))
        old_amount = o_list[my_index][0]
        if new_amount == 0:
            o_list.pop(my_index)
            print("_" * 50)
            print("{} is no longer apart of your order".format(name))
            print("_" * 50)
            edit_order_loop = False
        elif new_amount > 0:
            o_list[my_index][0] = new_amount
            new_price = new_amount*o_list[my_index][2]
            o_list[my_index][2] = new_price
            print("_" * 50)
            print("you now have {} {} instead of {} {}".format(new_amount, o_list[my_index][1], old_amount, o_list[my_index][1]))
            print("_" * 50)
            review_total_order(o_list)
            print("_" * 50)
            edit_order_loop = False
        else:
            print("invalid entry, try again")

def pick_up_or_drop_off(c_list, o_list):
    PDLoop = True
    while PDLoop is True:
        customer_name = get_string("Please enter your name for this order: ")
        recieving_food = get_string("{} would you like (P)ickup or (D)elivery?".format(customer_name))
        time = len(o_list)*20
        if recieving_food == "D":
            address = get_string("Please enter your street address to deliver to: ")
            temp_customerP = [customer_name, address, recieving_food]
            c_list.append(temp_customerP)
            print_list(c_list)
            PDLoop = False
        elif recieving_food == "P":
            print("_" * 50)
            print("{} please pickup your order from 132 Cuba Street, Te Aro, Wellington in {} mins".format(customer_name, time))
            print("_" * 50)
            temp_customerD = [customer_name, recieving_food]
            c_list.append(temp_customerD)
            print_list(c_list)
            PDLoop = False
        else:
            print("invalid entry, try again")

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

    # CHOOSE WHICH MENU YOU WANT
    print("_" * 50)
    choose_menu = get_integer("Select the number of the menu you would like to print ---> ")
    if choose_menu == 0:

        return pasta_menu
    elif choose_menu == 1:

        return vegan_menu
    elif choose_menu == 2:

        return antipasto_menu
    elif choose_menu == 3:

        return desserts_menu
    else:
        print("_" * 50)
        print("Invalid entry, try again")
        print("_" * 50)


def main():
    menu_list = [
            ["P", "Print menu"],
            ["O", "Order"],
            ["E", "Edit Order"],
            ["R", "Review Order"],
            ["Q", "Quit"]
        ]

    order_list = []

    customer_list = []

#  MENU LOOP
    menu_loop = True
    while menu_loop is True:

        print_list(menu_list)
        print("_"*50)

        # CHOOSE MENU OPTION : PRINT OR QUIT
        user_choice = get_string("Please select an option from the menu above --> ")
        print("_" * 50)

        # CHOICE P
        if user_choice == "P":
            menu = get_order_menu()
            print("_" * 50)
            print_with_price(menu)
            print("_" * 50)
        # CHOICE O
        elif user_choice == "O":
            menu = get_order_menu()
            print("_" * 50)
            order(menu, order_list)
            print("_" * 50)
            pick_up_or_drop_off(customer_list, order_list)
            print("_" * 50)
        #CHOICE E
        elif user_choice == "E":
            edit_order(order_list)
            print("_" * 50)
        # CHOICE Q
        elif user_choice == "R":
            review_total_order(order_list)
            print("_" * 50)

        elif user_choice == "Q":
            menu_loop = False
            print("Thank you for your time")
            print("_" * 50)

        else:
            print("Invalid entry, try again")
            print("_" * 50)


if __name__ == "__main__":
    main()



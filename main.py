# INPUTS
def get_integer(m):
    """
    This function allows the user to enter validated integer input, and not string
    :param m: question / message
    :return: integer
    """
    while True:
        try:
            my_integer = int(input(m))
            print("_" * 50)
            return my_integer
        except ValueError:
            print("please enter a number")
            print("_" * 50)
            continue


def get_integer_list_limit(m, l):
    """
    This function allows the user to enter validated integer
    input for lists, it has an input limit based on the length of the list
    :param m: question / message
    :param l: list that we are selecting an integer from, any list
    :return: integer
    """
    integer_loop = True
    while integer_loop is True:
        try:
            my_integer = int(input(m))
            print("_" * 50)
        except ValueError:
            # if the user doesn't enter a number
            print("please enter a number")
            print("_" * 50)
            continue
        if my_integer in range(0, len(l)):
            return my_integer
        else:
            # if the user enters number out of range
            print("invalid entry, the number you entered is not in the list")
            print("_" * 50)
            continue


def get_integer_dish_limit(m):
    """
    This function allows the user to enter validated integer input which is for the amount of a dish they want.
    This has limits of the most and least that they can order
    :param m: question / message
    :return: integer
    """
    min_ = 1
    max_ = 5
    integer_limit_loop = True
    while integer_limit_loop is True:
        try:
            my_integer = int(input(m))
            print("_" * 50)
        except ValueError:
            # if the user doesn't enter a number
            print("please enter a number")
            print("_" * 50)
            continue
        if my_integer in range(min_ - 1, max_ + 1):
            return my_integer
        else:
            # if the user orders too less or too many dishes
            print("invalid entry, you can only order between {} to {} of each dish".format(min_, max_))
            print("_" * 50)
            continue


def get_string(m):
    """Get a validated string from user input.
    param m: question / message
    return: string
    """
    while True:
        try:
            my_string = input(m)
            print("_" * 50)
            return my_string.upper().strip()
        except ValueError:
            # if the user doesn't enter an option from the list
            print("invalid entry, please enter one of the options")
            print("_" * 50)
            continue


def get_string_phone_limit(m):
    """
    This function allows the user to enter validated string input for their phone number,
    it has a limit on the min length the phone number can be and the max length.
    param m: question / message
    return: string
    """
    min_ = 3
    max_ = 20
    string_limit_loop = True
    while string_limit_loop is True:
        try:
            my_string = input(m)
            print("_" * 50)
        except ValueError:
            # if the user doesn't enter a long enough phone number
            print("please enter your phone number")
            print("_" * 50)
            continue
        # if input length is in range and it's numerical, return the string
        if len(my_string) in range(min_, max_) and my_string.isnumeric():
            return my_string
        else:
            # if input is more than maximum
            if len(my_string) > max_:
                print("it seems like your phone number is too long")
            # if input is not numerical
            elif not my_string.isnumeric():
                print("please enter your phone number")
            continue


def get_string_address_limit(m):
    """
    This function allows the user to enter validated string input for their address,
    it has a limit on the min length the address can be and the max length.
    param m: question / message
    return: string
    """
    min_ = 6
    max_ = 50
    string_limit_loop = True
    while string_limit_loop is True:
        try:
            my_string = input(m)
            print("_" * 50)
        except ValueError:
            # if the input is too small
            print("please enter your street address")
            print("_" * 50)
            continue
        if len(my_string) in range(min_, max_):
            return my_string
        else:
            # if input is too big
            if len(my_string) > max_:
                print("it seems like your street address is too long")
                print("_" * 50)
            continue


def get_string_name_limit(m):
    """
    This function allows the user to enter validated string input for their name,
    it has a limit on the min length their name can be and the max length.
    param m: question / message
    return: string
    """
    min_ = 2
    max_ = 20
    string_limit_loop = True
    while string_limit_loop is True:
        try:
            my_string = input(m)
            print("_" * 50)
        except ValueError:
            # if name is too short e.g 0 or 1 character, ask them to enter their name again
            continue
        if len(my_string) in range(min_, max_):
            return my_string
        else:
            # if the name is too long
            if len(my_string) > max_:
                print("this name is too long, enter your first name")
                print("_" * 50)
            continue


# REVIEW LISTS
def print_list(l):
    """
    This function is to prints 2 corresponding items in a list
    :param l: any list
    :return: None
    """
    for i in range(0, len(l)):
        output = "{:10} {:10}".format(l[i][0], l[i][1])
        print(output)


def print_list_2(c_list):
    """
        This function is to prints the customer details list,
         it prints different lists of a different length, depending on
         whether "P" / pickup or "D" / delivery is in the list
        :param c_list: customer details list
        :return: None
        """
    for i in range(0, len(c_list)):
        if "D" in c_list[i]:
            output = "{} : {:10} , {:10}, {}".format(c_list[i][0], c_list[i][1], c_list[i][2], c_list[i][3])
            print(output)

        elif "P" in c_list[i]:
            output = "{} : {:10}, {}".format(c_list[i][0], c_list[i][1], c_list[i][2])
            print(output)


def print_with_price(menu):
    """
    this function is to print the index number, the dish and the price
    param menu: any list, however, often menu list (list containing all the foods)
    return: None
    """
    for i in range(0, len(menu)):  # guarentees we go the end of the list and no further
        print("{} : {:<30} ${:.2f}".format(i, menu[i][0], menu[i][1]))


def print_with_indexes(f):
    """
    This function is supposed to print 1 item in a list, along with an index number
    :param f: food menu list
    :return: None
    """
    for i in range(0, len(f)):  # guarentees we go the end of the list and no further
        print("{} : {}".format(i, f[i][0]))


def print_order_with_indexes(o_list):
    """
    This is a print function, specifically meant for printing a dish / order, its amount and it's price with
    an index number
    :param o_list: order list
    :return: None
    """
    for i in range(0, len(o_list)):  # guarentees we go the end of the list and no further
        print("{} : {} {} ${}".format(i, o_list[i][0], o_list[i][1], o_list[i][2]))


def review_order(o_list):
    """
    This function is supposed to bring 1 item in the order list
    :param o_list: order list
    :return: None
    """
    output = "You have ordered {} {} for ${:.2f}".format(o_list[0], o_list[1], o_list[2])
    print(output)


def review_total_order(o_list, p, c_list):
    """
    This function is supposed to print the whole order list, customer list, as well as the grand total
    :param o_list: order list
    :param p: price list (list of prices, taken from the order list)
    :param c_list: customer info list
    :return: None
    """
    for i in range(0, len(o_list)):
        output = "You have ordered {} {} for ${:.2f}".format(o_list[i][0], o_list[i][1], o_list[i][2])
        print(output)
    print("your grand total: ${}".format(grand_total_calc(o_list, p, c_list)))
    print("_" * 50)
    print_list_2(c_list)

    # if D is in the list it will print "including $3
    for j in range(0, len(c_list)):
        if "D" in c_list[j]:
            print("including $3 delivery charge")
            print("_" * 50)


def grand_total_calc(o_list, p, c_list):
    """Here I am trying to calculate the grand total
    :param o_list: list (order list)
    :param p: list (list of prices, taken from the order list)
    :param c_list: list (list of customer information)
    :return:
    """
    # clear put and put in all prices again
    # avoids double ups
    # this is for if "D" / delivery is in the list
    p.clear()
    for i in range(0, len(c_list)):
        if "D" in c_list[i]:
            p.append(3)
        # IF ITS 'P' IN THE LIST IT CRASHES, this is if P is in the list
    for j in range(0, len(o_list)):
        # creating price list
        p.append(o_list[j][2])
    grand_total = sum(p)
    return grand_total


# CONFIRMATION
def stay_or_return(m="Do you want to (C)ontinue on this menu or (R)eturn to the main menu"):
    """
    I am trying to confirm whether the user wants to stay on the list that they are curerntly on,
    or go back to the main menu
    :param m: question / message
    :return: None
    """
    # do you want to order again
    # if not return None
    # running the loop
    getting_response = True
    while getting_response is True:
        response = get_string(m)
        print("_" * 50)
        if response not in ["C", "R"]:
            print("invalid entry, try again")
            print("_" * 50)
            continue
        elif response == "C":
            return True
        else:
            return False


# ORDERING
def order(menu, o_list):
    """
    User selects the list they want to order from, selects dish, the amount of the dish, and places an order
    :param menu: menu list (list of all the foods)
    :param o_list: order list
    :return: None
    """
    order_loop = True
    while order_loop is True:
        print_with_price(menu)
        print("_" * 50)
        if stay_or_return() is False:
            return None
        dish = get_integer_list_limit("Enter the number of the dish you would like to order ---> ", menu)
        print("_" * 50)
        name = menu[dish][0]
        amount = get_integer_dish_limit("How many would you like ---> ")
        print("_" * 50)
        price = menu[dish][1]
        total_price = price * amount
        temp_list = [amount, name, total_price]
        o_list.append(temp_list)
        review_order(temp_list)
        print("_" * 50)


# Editing Order
def edit_order(o_list, p, c_list):
    """
    change the quantity of pasta, we can delete
    :param o_list: order list
    :param p: list of prices, taken from the order list
    :param c_list: customer info list
    :return: None
    """
    # prints order
    print_order_with_indexes(o_list)
    print("_" * 50)
    my_index = get_integer_list_limit("Please enter the number of the dish you would like to edit / remove", o_list)
    print("_" * 50)
    # finds the name of the list
    name = o_list[my_index][1]
    # calculates the single price
    single_price = o_list[my_index][2]/o_list[my_index][0]
    # asks how much they want now
    new_amount = get_integer_dish_limit("How many {} do you want now? If you would like to remove this dish, "
                                        "please enter 0".format(o_list[my_index][1]))
    print("_" * 50)
    # finds old amount
    old_amount = o_list[my_index][0]
    if new_amount == 0:
        # deleting order
        o_list.pop(my_index)
        print("{} is no longer apart of your order".format(name))
        print("_" * 50)
    elif new_amount > 0:
        # finds new amount
        o_list[my_index][0] = new_amount
        # calculates new price
        new_price = new_amount*single_price
        # updates old price with new price
        o_list[my_index][2] = new_price
        grand_total_calc(o_list, p, c_list)
        print("you now have {} {} instead of {} {}, costing ${:.2f}".format(new_amount, o_list[my_index][1], old_amount,
                                                                            o_list[my_index][1], new_price))
        print("_" * 50)
    else:
        print("invalid entry, please enter a number")
        print("_" * 50)


# CUSTOMER DETAILS
def customer_details(c_list, o_list):
    """Get name phone from customer, find if delivery oor pickup, if so get address.

    param c_list: list (customer details)
    param o_list: list (2D ordered items)
    return: None
    """
    # if the user has already entered their order, confirms if they want to update them
    if len(c_list) > 0:
        re_enter = get_string("We already have your details, do you want to update them? (Y/N)")
        print("_" * 50)
        if re_enter == "Y":
            c_list.clear()
        elif re_enter == "N":
            return None
        else:
            print("invalid entry, try again")
            print("_" * 50)

    customer_name = get_string_name_limit("Please enter your first name for this order: ")
    print("_" * 50)
    customer_loop = True
    while customer_loop is True:
        recieving_food = get_string("{} would you like (P)ickup or (D)elivery ($3 delivery charge)?"
                                    .format(customer_name))
        print("_" * 50)
        time = len(o_list) * 15
        # for D we require name, phone, address
        if recieving_food == "D":
            customer_phone = get_string_phone_limit("Please enter your phone number: ")
            address = get_string_address_limit("Please enter your street address to deliver to: ")
            print("_" * 50)
            temp_d = [customer_name, address, customer_phone, recieving_food]
            c_list.append(temp_d)
            print("Your order will be delivered in {} mins".format(time))
            print_list_2(c_list)
            print("_" * 50)
            return False
        # for P we require name and phone
        elif recieving_food == "P":
            customer_phone = get_string_phone_limit("Please enter your phone number: ")
            print("{} please pickup your order from 132 Cuba Street, Te Aro, Wellington in {} mins"
                  .format(customer_name, time))
            print("_" * 50)
            temp_p = [customer_name, customer_phone, recieving_food]
            c_list.append(temp_p)
            print_list_2(c_list)
            print("_" * 50)
            return False
        else:
            # clear instructions
            print("invalid entry, enter P or D")
            print("_" * 50)
            continue


# User finishing their order
def finishing_order(c_list, o_list, c_l, p, m="Do you confirm your order and details (Y/N)"):
    """
    Finish ordering, enter final or last details that they forgot to enter before, confirm orders and details,
    clear list and start over
    :param c_list: customer info list
    :param o_list: order list
    :param c_l: confirm list (a list to store the users answers when confirm their order and details, e.d stores :
    "Y", "N"
    :param p: list of prices, taken from the order list
    :param m: question / message
    :return: None
    """
    finish_loop = True
    while finish_loop is True:
        # if they haven't ordered anything
        if len(o_list) == 0:
            print("You haven't ordered anything yet, please order first or if you want to quit enter "
                  "'Q' on the main menu")
            print("_" * 50)
            return None
        # if they haven't entered their customer details, make them enter
        elif len(c_list) == 0:
            customer_details(c_list, o_list)
            print("_" * 50)

        # clears list to prevent double-ups
        c_l.clear()
        review_total_order(o_list, p, c_list)
        print("_" * 50)
        # confirming order and details
        response = get_string(m)
        print("_" * 50)
        if response == "Y":
            c_l.append("Y")
            print("We are finishing you order now")
            print("_" * 50)
            print("Starting NEW order")
            print("_" * 50)
            # clearing all the lists to start a new order
            c_list.clear()
            o_list.clear()
            p.clear()
            c_l.clear()
        elif response == "N":
            return None
        else:
            print("invalid entry, please enter (Y/N)")
            continue


def get_order_menu():
    """
    lists of pasta menu, divided into food categories, e.g. vegan, desserts. User is also able to choose the menu they
    want to print / order from
    :return: None
    """
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
    print("_" * 50)

    # CHOOSE WHICH MENU YOU WANT
    choose_menu = get_integer_list_limit("enter the number of the menu you would like to print ---> ", food_menu)
    print("_" * 50)

    if choose_menu == 0:
        return pasta_menu
    elif choose_menu == 1:
        return vegan_menu
    elif choose_menu == 2:
        return antipasto_menu
    elif choose_menu == 3:
        return desserts_menu


def main():
    """
    the main code area, where the user chooses their actions from the main menu (e.g. order) and the program carries out
    those actions through calling various functions
    :return: None
    """
    menu_list = [
            ["P", "Print menu"],
            ["O", "Order"],
            ["E", "Edit Order"],
            ["R", "Review Order"],
            ["C", "Customer Details"],
            ["F", "Finish ordering"],
            ["Q", "Quit"]
        ]

    order_list = []

    customer_list = []

    price_list = []

    confirm_list = []

#  MENU LOOP
    menu_loop = True
    while menu_loop is True:

        print_list(menu_list)
        print("_" * 50)

        # CHOOSE MENU OPTION : PRINT OR QUIT
        user_choice = get_string("Please enter an option from the menu above --> ")
        print("_" * 50)

        # CHOICE P, print
        if user_choice == "P":
            menu = get_order_menu()
            print("_" * 50)
            print_with_price(menu)
            print("_" * 50)

        # CHOICE O, order
        elif user_choice == "O":
            menu = get_order_menu()
            print("_" * 50)
            order(menu, order_list)

        # CHOICE E, edit
        elif user_choice == "E":
            if len(order_list) > 0:
                edit_order(order_list, price_list, customer_list)
            else:
                print("you haven't ordered anything yet, please order first")
                print("_" * 50)

        # CHOICE R, review
        elif user_choice == "R":
            if len(order_list) > 0:
                review_total_order(order_list, price_list, customer_list)
            else:
                print("you haven't ordered anything yet, please order first")
                print("_" * 50)

        # CHOICE C, enter customer details
        elif user_choice == "C":
            customer_details(customer_list, order_list)

        # CHOICE F, finish ordering
        elif user_choice == "F":
            finishing_order(customer_list, order_list, confirm_list, price_list)

        # CHOICE Q, quit
        elif user_choice == "Q":
            menu_loop = False
            print("Thank you for your time")
            print("_" * 100)

        else:
            print("Invalid entry, try again")
            print("_" * 50)


if __name__ == "__main__":
    main()

# INPUTS
def get_integer(m):
    """
    This function allows the user to enter integer input, and not string
    :param m: integer input
    :return: integer
    """
    while True:
        try:
            my_integer = int(input(m))
            return my_integer
        except ValueError:
            print("please enter a number")
            print("_" * 50)
            continue

def get_integer_list_limit(m, l):
    """
    This function allows the user to enter integer input, and not string
    :param m: integer input
    :return: integer
    """
    integer_loop = True
    while integer_loop is True:
        my_integer = int(input(m))
        if my_integer in range(0,len(l)):
            return my_integer
        else:
            print("the number you entered is not in the list")
            print("_" * 50)
            continue

def get_integer_dish_limit(m):
    """
    This function allows the user to enter integer input, and not string
    :param m: integer input
    :return: integer
    """
    min_ = 1
    max_ = 6
    integer_limit_loop = True
    while integer_limit_loop is True:
        my_integer = int(input(m))
        if my_integer in range(min_, max_):
            return my_integer
        else:
            print("you can only order between {} to {} of each dish".format(min_, max_))
            print("_" * 50)
            continue

def get_string(m):
    """Get a validated string from user input.

    :param m: string input
    :return: string
    """
    while True:
        try:
            my_string = input(m)
            return my_string.upper().strip()
        except ValueError:
            print("invalid entry")
            print("_" * 50)
            continue

def get_string_phone_limit(m):
    """
    This function allows the user to enter integer input, and not string
    :param m: integer input
    :return: integer
    """
    min_ = 5
    max_ = 15
    string_limit_loop = True
    while string_limit_loop is True:
        my_string = int(input(m))
        if len(my_string) in range(min_,max_):
            return my_string
        else:
            if len(my_string) < 5:
                print("the phone number you have entered is too small")
            elif len(my_string) > 15:
                    print("the phone number you have entered is too big")
            continue

# REVIEW LISTS
def print_list(l):
    """
    This function is to tidely print 2 corresponding items in a list
    :param l: any list
    :return: output??
    """
    for i in range(0, len(l)):
        output = "{:10} {:10}".format(l[i][0], l[i][1])
        print(output)

def print_list_2(l):
    for i in range(0, len(l)):
        output = "{} : {:10} , {:10}".format(l[i][0], l[i][1], l[i][2])
        print(output)

def print_with_price(l):
    """
    this function is to print the index number, the dish and the price
    :param l: any list, often order list
    :return:
    """
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {:<30} ${:.2f}".format(i, l[i][0], l[i][1]))

def print_with_indexes(l):
    """
    This function is supposed to print 1 item in a list, along with an index number
    :param l: any list
    :return:
    """
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {}".format(i, l[i][0]))

def print_order_with_indexes(l):
    """
    This is a print function, specifically meant for printing a dish / order, its amount and it's price with an index number
    :param l: order_list
    :return:
    """
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {} {} ${}".format(i, l[i][0], l[i][1], l[i][2]))

def review_order(l):
    """
    This function is supposed to bring 1 item in the order list
    :param l: order_list
    :return:
    """
    output = "You have ordered {} {} for ${:.2f}".format(l[0], l[1], l[2])
    print(output)

def review_total_order(o_list, p, c_list):
    """
    This function is supposed to print the whole order list, as well as the grand total
    :param o_list:
    :param p:
    :param c_list:
    :return:
    """
    for i in range(0, len(o_list)):
        print_list_2(c_list)
        print("_" * 50)
        output = "You have ordered {} {} for ${:.2f}".format(o_list[i][0], o_list[i][1], o_list[i][2])
        print(output)
    print( "your grand total: ${}".format( grand_total_calc(o_list, p, c_list) ) )
    print("_" * 50)

def grand_total_calc(o_list,p, c_list):
    """Here I am trying to calculate the grand total
    :param o_list: list (order list)
    :param p: list (list of prices, taken from the order list)
    :param c_list: list (list of customer information)
    :return:
    """
    # clear put and put in all prices again
    # avoids double ups
    p.clear()
    for i in range(0, len(c_list)):
        if "D" in c_list[i]:
            p.append(3)
        # IF ITS 'P' IN THE LIST IT CRASHES
    for j in range(0, len(o_list)):
        # creating price list
        p.append(o_list[j][2])
    grand_total = sum(p)
    return grand_total


# CONFIRMATION
def stay_or_return(m = "Do you want to (C)ontinue on this menu or (R)eturn to the main menu"):
    """
    I am trying to confirm whether the user wants to stay on the list that they are curerntly on, or go back to the main menu
    :param m: string message
    :return:
    """
    # do you want to order again
    # if not return None
    # running the loop
    getting_response = True
    while getting_response is True:
        response = get_string(m)
        if response not in ["C", "R"]:
            print("invalid entry, try again")
            continue
        elif response == "C":
            return True
        else:
            return False

# ORDERING
def order(m, o_list):
    """
    User selects the list they want to order from, selects dish, the amount of the dish, and places an order
    :param m: string message
    :param o_list: order_list
    :return:
    """
    order_loop = True
    while order_loop is True:
        print_with_price(m)
        print("_" * 50)
        if stay_or_return() is False:
            return None
        dish = get_integer_list_limit("Enter the number of the dish you would like to order ---> ", m)
        print("_" * 50)
        name = m[dish][0]
        amount = get_integer_dish_limit("How many would you like ---> ")
        print("_" * 50)
        price = m[dish][1]
        total_price = price * amount
        temp_list = [amount, name, total_price]
        o_list.append(temp_list)
        review_order(temp_list)
        print("_" * 50)

def edit_order(o_list,p, c_list):
    """
    change the quantity of pasta, we can delete
    :param o_list: order_list
    :param p: price_list
    :param c_list: customer_list
    :return:
    """
    print_order_with_indexes(o_list)
    print("_" * 50)
    my_index = get_integer_list_limit("Please enter the number of the dish you would like to edit / remove", o_list)
    name = o_list[my_index][1]
    single_price= o_list[my_index][2]/o_list[my_index][0]
    new_amount = get_integer("How many {} do you want now? If you would like to remove this dish, please enter 0".format(o_list[my_index][1]))
    print("_" * 50)
    old_amount = o_list[my_index][0]
    if new_amount == 0:
        o_list.pop(my_index)
        print("{} is no longer apart of your order".format(name))
        print("_" * 50)
    elif new_amount > 0:
        o_list[my_index][0] = new_amount
        new_price = new_amount*single_price
        o_list[my_index][2] = new_price
        grand_total_calc(o_list, p, c_list)
        print("you now have {} {} instead of {} {}, this costs ${:.2f}".format(new_amount, o_list[my_index][1], old_amount, o_list[my_index][1], new_price))
        print("_" * 50)
    else:
        print("invalid entry, try again")

#CUSTOMER DETAILS
def customer_details(c_list, o_list):
    """Get name phone from customer, find if delivery oor pickup, if so get address.

    :param c_list: list (customer details)
    :param o_list: list (2D ordered items)
    :return: None
    """
    if len(c_list) > 0:
        re_enter = get_string("We already have your details, do you want to update them? (Y/N)")
        if re_enter == "Y":
            c_list.clear()
        elif re_enter == "N":
            return None
        else:
            print("invalid entry, try again")

    customer_name = get_string("Please enter your name for this order: ")
    recieving_food = get_string("{} would you like (P)ickup or (D)elivery?".format(customer_name))
    customer_phone = get_string_phone_limit("Please enter your phone number: ")
    time = len(o_list) * 20
    if recieving_food == "D":
        address = get_string("Please enter your street address to deliver to: ")
        print("_" * 50)
        temp_D = [customer_name, address, customer_phone, recieving_food]
        c_list.append(temp_D)
    elif recieving_food == "P":
        print("{} please pickup your order from 132 Cuba Street, Te Aro, Wellington in {} minsO".format(customer_name,time))
        print("_" * 50)
        temp_P = [customer_name, customer_phone, recieving_food]
        c_list.append(temp_P)
    print_list_2(c_list)

#User finishing their order
def finishing_order(c_list, o_list, c_l, p, m="Do you confirm your order and details (Y/N)"):
    """
    Finish ordering, enter final or last details that they forgot to enter before, confirm orders and details, clear list and start over
    :param c_list: customer_list
    :param o_list: order_list
    :param c_l: confirm_o_list
    :return:
    """
    if len(o_list) == 0:
        print("You haven't ordered anything yet, please order first or if you want to quit enter 'Q' on the main menu")
        print("_" * 50)
        return None
    elif len(c_list) == 0:
        customer_details(c_list, o_list)
        print("_" * 50)

    # do you want to order again
    # if not return None
    c_l.clear()
    review_total_order(o_list, p, c_list)
    print("_" * 50)
    response = get_string(m)
    print("_" * 50)
    if response == "Y":
        c_l.append("Y")
        print("_" * 50)
        print("We are finishing you order now")
        print("Starting New order")
        print("_" * 50)
        c_list.clear()
        o_list.clear()
        p.clear()
        c_l.clear()
    elif response == "N":
        return None

def get_order_menu():
    """
    lists of pasta menu, divided into food categories, e.g vegan, desserts. User is also able to choose the menu they want to print / order from
    :return:
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
    the main code area, where the user chooses their actions from the main menu (e.g order) and the program carries out those actiomns through functions
    :return:
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

        #CHOICE E
        elif user_choice == "E":
            if len(order_list) > 0:
                edit_order(order_list, price_list, customer_list)
                print("_" * 50)
            else:
                print("you havent ordered anything yet, please order first")
                print("_" * 50)

        elif user_choice == "R":
            if len(order_list) > 0:
                review_total_order(order_list, price_list, customer_list)
                print("_" * 50)
            else:
                print("you havent ordered anything yet, please order first")
                print("_" * 50)

        elif user_choice == "C":
            customer_details(customer_list, order_list)
            print("_" * 50)

        elif user_choice == "F":
            finishing_order(customer_list, order_list, confirm_list, price_list)

        elif user_choice == "Q":
            menu_loop = False
            print("Thank you for your time")
            print("_" * 50)

        else:
            print("Invalid entry, try again")
            print("_" * 50)


if __name__ == "__main__":
    main()



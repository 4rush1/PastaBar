def get_integer(l):
    integer_loop = True
    while integer_loop is True:
        try:
            my_integer = int(input(l))
            return my_integer
        except ValueError:
            print("Invalid entry, please enter a number")
            continue

def get_integer_list_limits(m, min_, max_):
    return None

def get_string(l):
    my_string = input(l)
    return my_string.upper

def print_order_with_indexes(l):
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {} {}".format(i, l[i][0], l[i][1]))

def get_confirmation(m = "Do you want to continue on this menu (C) or return back the main menu (R)"):
    response = input(m)
    while response not in ["C", "R"]:
        print("This is not a recognised entry")
        return False
    if response == "C":
        return True
    elif response == "R":
        return False

def get_confirmation_customer_details(m = "We already have your details, do you want to (C)ontinue and update your details or (R)eturn"):
    response = input(m)
    print("_" * 50)
    while response not in ["C", "R"]:
        print("invalid entry, try again")
        continue
    if response == "C":
        return True
    elif response == "R":
        return None



#def my_grand_total(l):
    #for i in range(0, len(l)):
       # grand_total = sum(l[i][1])
       # print("your total bill is {:.2f}".format(grand_total))
   # return None

#incorperating the grand total into the review order
def review_total_order(l, p):
    for i in range(0, len(l)):
        # prints the the dish l[i][0], amount l[i][1] and price l[i][2]
        output = "You have ordered {} {} for ${:.2f}".format(l[i][0], l[i][1], l[i][2])
        print(output)
        #p.append(l[i][2])
        #single_price = l[i][2] / l[i][1]
    #price_list = [i , single_price] DONT NEED THESE
    #print(p)
    #grand_total = sum(p)
    #print(grand_total)

def grand_total(l,p, c_list):
    """Here I am trying to calculate the grand total
    :param l: list (order list)
    :param p: list (list of prices)
    :return:
    """
    print("clear")
    p.clear()
    print(p)
    for x in range(0, len(c_list)):
        if c_list[x][3] == "D":
            print("add 3")
            p.append(3)
            print(p)
            print("total list")
    for i in range(0, len(l)):
        #creating price list
        p.append(l[i][2])
        grand_total = sum(p)
    print(p)
    print(grand_total)

def confirm(c, o_list, m = "Do you confirm this order (Y/N)"):
    # do you want to order again
    # if not return None
    response = get_string(m)
    print("_" * 50)
    if response == "Y":
        c.append("Y")
        return False
    elif response == "N":
        c.append("N")
        edit = get_string("Do you want to edit your order (Y/N)? ")
        if edit =="Y":
            edit_order(o_list)
        elif edit =="N":
            return False

def customer_details(c_list, o_list, p):
    """Get name phone from customer, find if delivery oor pickup, if so get address.

    :param c_list: list (customer details)
    :param o_list: list (2D ordered items)
    :return: None
    """
    #if len(c_list) > 0:
       # re_enter = get_string("We already have your details, do you want to update them? (Y/N)")
        #if re_enter == "Y":
         #   c_list.clear()
      #  elif re_enter == "N":
       #     return None
      #  else:
      #      print("invalid entry, try again")

    customer_name = get_string("Please enter your name for this order: ")
    recieving_food = get_string("Would you like (P)ickup or (D)elivery?")
    customer_phone = get_integer("Please enter your phone number: ")

    if recieving_food == "D":
        address = get_string("Please enter your street address to deliver to: ")
        print("_" * 50)
        temp_D = [customer_name, address, customer_phone, recieving_food]
        c_list.append(temp_D)
        print(c_list)
        p.append(3)
        print(p)

    elif recieving_food == "P":
        time = len(o_list) * 20
        print("{} please pickup your order from 132 Cuba Street, Te Aro, Wellington in {} mins".format(customer_name,time))
        print("_" * 50)
        temp_P = [customer_name, customer_phone, recieving_food]
        c_list.append(temp_P)

    print(c_list)

def edit_order(o_list):
    print_order_with_indexes(o_list)
    print("_" * 50)
    my_index = get_integer("Please enter the number of the dish you would like to edit / remove")
    name = o_list[my_index][1]
    new_amount = get_integer("How many {} do you want now? If you would like to remove this dish, please enter 0".format(o_list[my_index][1]))
    print("_" * 50)
    old_amount = o_list[my_index][0]
    if new_amount == 0:
        o_list.pop(my_index)
        print("{} is no longer apart of your order".format(name))
        print("_" * 50)
    elif new_amount > 0:
        o_list[my_index][0] = new_amount
        new_price = new_amount*o_list[my_index][2]
        o_list[my_index][2] = new_price
        print("you now have {} {} instead of {} {}".format(new_amount, o_list[my_index][1], old_amount, o_list[my_index][1]))
        print("_" * 50)
    else:
        print("invalid entry, try again")

def main():
    list1 = [
        ["food1", 20, 45],
        ["food2", 40, 80]
    ]

    price_list = [3, 4, 5, 6]

    customer_list = [
        ["Dave", "34A Dave Street", "23456543234567", "D"]
    ]

    confirm_list = []

    #pick_up_or_drop_off(customer_list, order_list)

    #name = get_string("Hello, whats your name:")
    #print(name)

    #review_total_order(list1, price_list)
    #customer_details(customer_list, list1, price_list)
    #grand_total(list1, price_list, customer_list)

    confirm(confirm_list, list1)


main()



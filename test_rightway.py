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
    return my_string


def get_confirmation(m = "Do you want to continue on this menu (C) or return back the main menu (R)"):
    response = input(m)
    while response not in ["C", "R"]:
        print("This is not a recognised entry")
        return False
    if response == "C":
        return True
    else:
        return False

def my_grand_total(l):
    for i in range(0, len(l)):
        grand_total = sum(l[i][1])
        print("your total bill is {:.2f}".format(grand_total))
        return None

def pick_up_or_drop_off(c_list, o_list):
    if len(c_list) == 0:
        customer_name = get_string("Please enter your name for this order: ")
        recieving_food = get_string("{} would you like (P)ickup or (D)elivery?".format(customer_name))
        customer_phone = get_integer("Please enter your phone number: ")
        time = len(o_list)*20
        if recieving_food == "D":
            address = get_string("Please enter your street address to deliver to: ")
            print("_" * 50)
            temp_P = [customer_name, address, customer_phone]
            c_list.append(temp_P)
            print(c_list)
        elif recieving_food == "P":
            print("{} please pickup your order from 132 Cuba Street, Te Aro, Wellington in {} mins".format(customer_name, time))
            print("_" * 50)
            temp_D = [customer_name, customer_phone]
            c_list.append(temp_D)
            print(c_list)
    elif len(c_list) == 0:
        print("We already have your details")
        return False

def main():
    list1 = [
        ["food", 20],
        ["food2", 40]
    ]

    customer_list = [
    ]

    order_list = [
        ["food"]
    ]

    pick_up_or_drop_off(customer_list, order_list)



main()



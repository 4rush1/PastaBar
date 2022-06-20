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


def print_with_indexes(l):
    for i in range(0, len(l)):  # guarentees we go the the end of the list and no further
        print("{} : {:<30} ${:.2f}".format(i, l[i][0], l[i][1]))


def review_pasta(l):
    print_with_indexes(l)
    print("-" * 50)


def main():
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

    menu_list = [
        ["P", "Print menu"],
        ["Q", "Quit"]
    ]

    food_menu = [
        [1, "Pasta"],
        [2, "Vegan"],
        [3, "Antipasto"],
        [4, "Desserts"],
    ]

#  MENU LOOP
    menu_loop = True
    while menu_loop is True:
        print_list(menu_list)
        print("-" * 50)
        # CHOOSE MENU OPTION : PRINT OR QUIT
        user_choice = get_string("Please select an option from the menu above --> ")
        # CHOICE P
        if user_choice == "P":
            print("-" * 50)
            print_list(food_menu)
            print("-" * 50)
            # CHOOSE WHICH MENU YOU WANT
            choose_menu = get_integer("Select the number of the menu you would like to print ---> ")
            if choose_menu == 1:
                print("-" * 50)
                review_pasta(pasta_menu)
            elif choose_menu == 2:
                print("-" * 50)
                review_pasta(vegan_menu)
            elif choose_menu == 3:
                print("-" * 50)
                review_pasta(antipasto_menu)
            elif choose_menu == 4:
                print("-" * 50)
                review_pasta(desserts_menu)
            else:
                print("-" * 25)
                print("invalid entry, try again")
                print("-" * 50)
        # CHOICE Q
        elif user_choice == "Q":
            menu_loop = False
            print("-" * 50)
            print("thank you for participating")
        else:
            print("-" * 25)
            print("invalid entry, try again")
            print("-" * 50)

if __name__ == "__main__":
    main()



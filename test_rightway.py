def get_integer(l):
    while True:
        try:
            my_integer = int(input(l))
            return my_integer
        except:
            print("Invalid entry, please enter a number")

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

def main():
    list1 = [
        ["food", 20],
        ["food2", 40]
    ]

    my_grand_total(list1)

main()



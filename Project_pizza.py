print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small=15
cheese=1
medium=20
large=25

if size=="S":
    if add_pepperoni=="Y":
        smallpepperoni=2
        if extra_cheese=="Y":
              total=small+cheese+smallpepperoni
              print(f"Total price:${total}")
        else:
            total=smallpepperoni+small
            print(f"Total price=${total}")
    else:
        total=small
        print(f"Total price ${total}")
if size=="M":
    if add_pepperoni=="Y":
        mediumpepperoni=3
        if extra_cheese=="Y":
            total=medium+mediumpepperoni+cheese
            print(f"Total price ${total}")
        else:
            total=medium+mediumpepperoni
            print(f"Total price ${total}")
    else:
        total=medium
        print(f"Total price:${total}")
if size=="L":
    if add_pepperoni=="Y":
        largepepperoni=3
        if extra_cheese=="Y":
            total=large+largepepperoni+cheese
            print(f"Total price ${total}")
        else:
            total=large+largepepperoni
            print(f"Total price ${total}")
    else:
        total=large
        print(f"Total price:${total}")




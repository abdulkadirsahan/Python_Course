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
#---------------------------------------------------------------+--------------------------------------------------------------------

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.") 




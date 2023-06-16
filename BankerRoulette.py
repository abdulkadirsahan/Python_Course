import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

tp=len(names)
rndm=random.randint(0,tp-1)
rndmprsn=names[rndm]

print(rndmprsn + " You will pay")


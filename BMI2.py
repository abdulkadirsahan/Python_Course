height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi=round((weight)/(height**2),2)


if bmi<18.5:
    print(f"BMİ {bmi} you are in the weak group.")

elif bmi<25:
    print(f"BMİ {bmi} NYou are in a normal group.")

elif bmi<30:
    print(f"BMİ {bmi} you're in the slightly overweight group.")

elif bmi<35:
    print(f"BMİ {bmi} you are in the obese group.")
    
else:
    print(f"BMİ {bmi} you are in the clinical obese group.")
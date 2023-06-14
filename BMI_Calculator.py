heigh=float(input("Enter your height: "))
weigh=int(input("Enter your weigh: "))


#the number written on the right side of the comma indicates how many digits the decimal part will have.


bmi=round((weigh)/(heigh**2),2) #round, to the nearest number in rounding.
print(bmi)
age=int(input("What is your current age: "))

years=90-int(age)

days=round(years*365)
weeks=(years*52)
months=(years*12)
#print(f"..") ---> It is an operator of the expression written in fancy brackets ({}) in f-string expressions.

print(f"There are {days} days,{weeks} weeks,{months} months left until you turn 90.") 
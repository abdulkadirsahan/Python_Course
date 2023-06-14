print("   WELCOME   ")

bill=float(input("How much is the totall bill? "))

tip=int(input("What percentage do you want to pay? 12,15 or 18? "))

people=int(input("How many people will split the tip? ")) 


tip_as_percent=tip/100

total_tip_amount=bill*tip_as_percent

total_bill=bill + total_tip_amount
bill_per_person=total_bill / people
final_amount=round(bill_per_person,2)

print(f"Each person should pay : {final_amount}")




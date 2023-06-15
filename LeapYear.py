
year = int(input("Which year do you want to check? "))

if year%4==0:
    if year%100==0:
        if year&400==0:
            print("Leap year.")
        else:
            print("Not leap year.")       # if'i iç içe yazarken 2.if i eklediğin de 1.satıra elseyi ekle ve 2.if den devam et.
    else:
        print("Leap year.")                 #İç içe if'lerde pc ilk olarak büyük resme bakar.Sonra if deyiminin içindeki iç içe geçmiş                                           #bloğa
else:                                       #bloğa mı girmesi gerektiğine karar verir.
    print("Not leap year.")






      

    


    

      
    
   
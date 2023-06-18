student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)

high_score=0

for score in student_scores:    #Bu satırdaki score tekilden çoğula artışı temsil ediyor.
  if score>high_score:          #Yani listedeki her bir veriyi bir kere döndürüyor.Sonra diğerine geçiyor.
    high_score=score            #Score burada bir değişken olarak belirlenmiş oldu.

print(f"{high_score}")




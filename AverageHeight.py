student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total=0
for height in student_heights:
  total+=height
print(f"Total height: {total}")
  
number_of_student=0
for student in student_heights:
  number_of_student+=1
print(f"Number of student: {number_of_student}")

avarage=round(total/number_of_student)
print(f"Student heigh of avarage: {avarage}")

#sum() fonksiyonu ile listedeki tüm öğelerin toplamını bulabiliriz.
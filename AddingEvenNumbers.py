#2 + 4 + 6 + 8 +10 ... + 98 + 100

even=0
for number in range(2,102,2):
    even+=number
    number=even
print(even)
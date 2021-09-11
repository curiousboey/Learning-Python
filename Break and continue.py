number = 0

while number < 10:
    if number == 5:
       break #break whenever number = 5
    number += 1
    print(number)

number2 = 0
while number2 < 10:
    number2 += 1
    if number2 < 5:
       continue #number less than 5 loop continue
    print(number2)

for n in [1, 2, 3, 4, 5]:
    if n <5:
        continue
    print(n)
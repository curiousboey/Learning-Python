import math

def add(x,y):
   return x+y

print(math.sqrt(81))
print(4*math.pi)

def convert_gender(gender:str):
   gender =gender.upper()
   if gender == "M":
      return "FEMALE"
   elif gender == "F":
      return "MALE"
   else:
      return "UNKNOWN"

print(convert_gender("M"))
print(convert_gender("f"))
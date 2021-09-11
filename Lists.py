# number = 1
# number_two = 2
# number_three = 3

numbers = [1, 2, 3, 4, -1, 0, ['A', 2.1, "suruchi"]] #lists
print(numbers[0], "and", numbers[3]) #index 0 and 3
print(numbers[6][2])


#useful list methods
numbers.append(1000)
print(numbers)
print(len(numbers))
print(1000 in  numbers)

#deleting  items from lists
numbers.remove(1)
numbers.pop() # delete last entry
print(numbers)


del numbers[0:2] #delete upto index 1, 2 is exclusive
print(numbers)










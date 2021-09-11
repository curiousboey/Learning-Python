file = open('./data.csv', 'r+') #create csv file
# r+ for read and write
# w for writing
# a for appending
# r for reading
file.write("id,name,email\n")
file.write("suruchi,25,kumarigal\n")
file.close()

#better way to work with files
with open("./data.csv", 'r') as file:
    print(file.read())

import os.path
filename = "./dataaa.csv"
if os.path.isfile(filename):
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f'{filename} doesnot exit')
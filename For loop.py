names= ['suruchi', 'Bhupendra', 'ram', 'hari']

for name in names:
    print(name)

#loop through dictionaries

person = {
    "name": "suruchi",
    "age": 25,
    "address": "kumarigal"
}
for key in person:
    print(f'key:{key} value:{person[key]}')

print(person['age'])
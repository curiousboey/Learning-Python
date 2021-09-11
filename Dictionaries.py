person = {
    "name": "suruchi",
    "age": 25,
    "address": "kumarigal"
}
# name is key and suruchi is value and key must be unique
print(person["name"])
print(person["address"])

print(person.values())
print(person.keys())
print(person.get("age"))
person["age"] = 28
print(person)
brand = "amigoscode"
print(brand.upper())
print(brand.replace('a','33'))
print(len(brand))
print(brand == "Amigoscode")
print("code" in brand)
print("code" not in brand)

# multiline and formatting strings
name = "suruchi"
age = 22
comment = """
hello {}
how are you?
It was nice talking to you
age {}
"""
print(comment.format(name,age))

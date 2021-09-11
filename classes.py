class phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f'{self.brand} is calling {phone_number}')

iphone = phone('Iphone 7+', 300)
samsung = phone('samsung s20', 1400)
print(iphone.brand)
print(iphone.price)
iphone.call('999')


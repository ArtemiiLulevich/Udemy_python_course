class Kettle:

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 8.99)
print(kenwood.make)

kenwood.switch_on()

print('{0.make} - {0.price} - {0.on}'.format(kenwood))

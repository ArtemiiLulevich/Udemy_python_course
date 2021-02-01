import Part_10_Object_Oriented_Python.ducks as ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck_3 = ducks.Duck()
duck_4 = ducks.Duck()
duck_5 = ducks.Duck()
duck_6 = ducks.Duck()
duck_7 = ducks.Duck()
percy = ducks.Penguin()


flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck_3)
flock.add_duck(percy)
flock.add_duck(duck_5)
flock.add_duck(duck_6)
flock.add_duck(duck_7)
flock.add_duck(duck_4)


flock.migration()

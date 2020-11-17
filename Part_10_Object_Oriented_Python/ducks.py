class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard...")
        else:
            print("I'll just walk.")


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("top, top, top")
        return

    def swim(self):
        print("In water...")
        return

    def quack(self):
        print("Quack quack")
        return

    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("top, top, top too")
        return

    def swim(self):
        print("In water... Cooooold")
        return

    def quack(self):
        print("I'm a penguin!")
        return


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()

    donald.fly()

    # test_duck(donald)
    # test_duck(percy)

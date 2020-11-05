import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._basic_hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{} took {} points damage and have {} HP left".format(self._name, damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                self._hit_points = self._basic_hit_points
                print("{0._name} lost the life".format(self))
            else:
                self._hit_points = 0
                self._alive = False
                print("{0._name} dies. You win!".format(self))

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you.".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def levitation(self):
        print("{0._name} flies!!!".format(self))

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140
        self._basic_hit_points = 140

    def take_damage(self, damage):
        damage //= 4
        super().take_damage(damage=damage)

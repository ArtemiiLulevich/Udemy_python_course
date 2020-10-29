from player import Player

artem = Player("Artem")

print(artem.name)
print(artem.lives)

# print(artem)
# artem.lives -= 1
#
# print(artem)
# artem.lives -= 1
#
# print(artem)
# artem.lives -= 1
#
# print(artem)
# artem.lives -= 1


artem.level += 1
print(artem)

artem.level += 3
print(artem)

artem.level -= 5
print(artem)

artem.level = 5
print(artem)

artem.score = 500
print(artem)

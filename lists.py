friends = ["Alpha", "Bravo", "Charlie", "Delta"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:2])
friends[1] = "Foxtrot"
print(friends)

new_friends = ["Golf", "Hotel"]
friends.extend(new_friends)
print(friends)

lucky_numbers = [4,8,15,23, 42]
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
friends2.reverse()
print(friends2)
print(friends)

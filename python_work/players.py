players = ['charles', 'martina', 'michael', 'florence', 'eli']

#print(players[0:3])
print(players[:3])

print(players[2:])

print(players[-3:])

print("Here are the firts three players on my team:")
for player  in players[:3]:
    print(player.title())
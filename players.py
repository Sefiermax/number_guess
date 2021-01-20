players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
print('Here is the first three players:')

for player in players[:3]:
	print(player.title())




print(f'The first three items in the list are:\n{players[:3]}')
print(f'Three items from the middle of the list are:\n{players[1:4]}')
print(f'The last three items in the lsit are:\n{players[2:5]}')




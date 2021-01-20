motorcycle = ['honda', 'yamaha', 'suzuki']		#
print(motorcycle)

motorcycle[0] = 'ducati'						#
print(motorcycle)

motorcycle[0] = 'honda'							#
print(motorcycle)

motorcycle.append('ducati')						#
print(motorcycle)								#____________________________________________________________________________

motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.insert(0, 'ducati')
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
del motorcycle[0]
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
popped_motorcycle = motorcycle.pop()
print(popped_motorcycle)
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycle.pop()
msg = f"The first motorcycle I owned was a {last_owned.title()}."
print(msg)

motorcycle = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycle.pop(0)
msg = f"The first motorcycle I owned was a {first_owned.title()}."
print(msg)

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycle.remove('ducati')
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(f'\nA {too_expensive.title()} is too expensive for me.')
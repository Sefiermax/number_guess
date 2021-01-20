pizzas = ['pepperoni', 'plain', 'buffalo chicken','sausage']
print(pizzas)

fpizzas = pizzas[:]
print(fpizzas)

print(f'\nMy favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print(f"\nMy friend's favorite pizzas are:")
for fpizza in fpizzas:
	print(fpizza)
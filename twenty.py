twenty = [count * 1 for count in range(1,21)]
print(twenty)


million = list(range(1,1_000_001))
print(min(million))
print(max(million))
print(sum(million))


odd_numbers = list(range(1,20,2))
for number in odd_numbers:
	print(number)


threes = list(three * 3 for three in range(3,31))
print(threes)

cubed = []
for value in range(11):
	cube = value ** 3
	cubed.append(cube)
print(cubed)

cubed = [num**3 for num in range(1,11)]
print(cubed)














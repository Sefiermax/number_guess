import random

def guess(x):
	random_number = random_randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess < random_number:
			print('Sorry, guess again, too low.')
		elif guess > random_number:
			print('Sorry, guess again, too high')

def computer_guess(x):
	low = 1
	high = x
	feedback = ""
	while feedback !='C':
		guess = random.randint(low, high)
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
		if feedback == "h":
			high = guess -1
		elif feedback == 'l':
			low = guess +1

print(f'Muwhahahah! Your number MUST BE {guess} Skynet is real and here is my proof!')

guess(3)
import time
import os
import random
psr_list = ['paper', 'scissors', 'rock']
x = True
while x:
	starting_choice = input('\nhello logan what do you want to do today?\n1)play paper scissors rock?\n2)have a convosation?\n3)play hang man\ne) exit\n1,2,3 or e: ')

	if starting_choice == '1':
		os.system('clear')
		psr = True
		while psr:
				choice = input('e to exit\npaper, scissors or rock?: ')
				if choice == 'paper':
					if (random.choice(psr_list)) == 'paper':
						print('its a tie')
					elif (random.choice(psr_list)) == 'rock':
						print('i got rock, dam')
					else:
						print('HAH i win :D')
				elif choice == 'scissors':
					if (random.choice(psr_list)) == 'paper':
						print('dam you win')
					elif (random.choice(psr_list)) == 'scissors':
						print('its a dual then')
					else:
						print('HAHA i win :)')
				elif choice == 'rock':
					if (random.choice(psr_list)) == 'paper':
						print('I WIN heheheha')
					elif (random.choice(psr_list)) == 'scissors':
						print('you win :(')
					else:
						print('well well well its a tie')
				elif choice == 'e':
					psr = False
				else:
					print('sorry thats not an option')
	elif starting_choice == '2':
		os.system('clear')
		print('this will be a random word combo')
	elif starting_choice == '3':
		os.system('clear')
		print('this will be hangman (if i can figure it out(without a guide))')
	elif starting_choice == 'e':
		os.system('clear')
		print('goodbye')
		x = False
		break
	else:
		os.system('clear')
		print('sorry that isnt an option')



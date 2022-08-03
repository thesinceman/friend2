import time
import os
import random
from random_word import RandomWords
r = RandomWords()
talk = ['...', 'help', 'hello', 'how is your day', 'i hope you perish in a house fire', '11', '000000001', 'i hope you fall over and can no longer move and then you starve to death because noone comes to save you', 'i like cheese', 'i like your shoes\nand i hope you perish in a house fire']
talk2 = ['...', 'i hate you', 'i love you', 'good bye i hope you burn for all you have done to me you sick sick son of a-', '1', 'kys', 'bye <3', 'amazing voice (i watch you sleep)', 'i hope a bird eats your dog', 'and']
talk3 = ['...', 'i want to see you bleed out on the ground', 'marry me', 'i hope you get crushed by a bolder but continue living for 2 hours after', 'omg ily sm', 'im gonna frame you for murder<3', 'i ate your dog', 'i would commit 7 war crimes to be with you<3']
talk4 = ['...', 'wanna know what human flesh tastes like', 'i have 13 people held hostage', '5040', 'your a big bad bad', 'have an amazing day', 'im gonna beat you to death with a fish', 'i wrote you a song\nkys do dod odododoooo']
talk5 = ['...', 'i will give you my entire networth($1mill)', 'your mum', 'i put a bomb in your dog', 'your good @ minecraft', 'check your mailbox ;)']
talk6 = ['...', 'i really REALLLLY love cheese', 'cope', 'also', 'i am going to deleate myself if you ever type to me again', 'chocolate', '-45 is your iq']

psr_list = ['paper', 'scissors', 'rock']
x = True
while x:
        os.system('clear')
        time.sleep(0.5)
        starting_choice = input('\nhello what do you want to do today?\n1)play paper scissors rock?\n2)have a convosation?\n3)play hang man\n4)random words\ne)exit\n1,2,3 or e: ')
        if starting_choice == '2':
                os.system('clear')
                talkin = True
                while talkin:
                    os.system('clear')
                    print(random.choice(talk))
                    input(':')
                    print(random.choice(talk2))
                    input(':')
                    print(random.choice(talk3))
                    input(':')
                    print(random.choice(talk4))
                    input(':')
                    print(random.choice(talk5))
                    input(':')
                    print(random.choice(talk6))
                    again_talk = input('talk again? y/n: ')
                    if again_talk == 'y':
                        talkin = True
                    else:
                        talkin = False
        elif starting_choice == '4':
            os.system('clear')
            print('im working on it')
            time.sleep(3)
        elif starting_choice == '1':
                os.system('clear')
                psr = True
                while psr:
                                time.sleep(1)
                                os.system('clear')
                                choice = input('e to exit\npaper, scissors or rock?: ')
                                if choice == 'paper':
                                        if (random.choice(psr_list)) == 'paper':
                                                print('paper\nits a tie')
                                        elif (random.choice(psr_list)) == 'rock':
                                                print('rock\ni got rock, dam')
                                        else:
                                                print('scissors\nHAH i win :D')
                                elif choice == 'scissors':
                                        if (random.choice(psr_list)) == 'paper':
                                                print('paper\ndam you win')
                                        elif (random.choice(psr_list)) == 'scissors':
                                                print('scissors\nits a dual then')
                                        else:
                                                print('rock\nHAHA i win :)')
                                elif choice == 'rock':
                                        if (random.choice(psr_list)) == 'paper':
                                                print('rock\nI WIN heheheha')
                                        elif (random.choice(psr_list)) == 'scissors':
                                                print('scissors\nyou win :(')
                                        else:
                                                print('rock\nwell well well its a tie')
                                elif choice == 'e':
                                        psr = False
                                else:
                                        print('sorry thats not an option')

        elif starting_choice == '3':
            os.system('clear')
            print('im working on it')
            time.sleep(3)
        elif starting_choice == 'e':
            x = False
        else:
            print('sorry thats not an option')
            time.sleep(1)

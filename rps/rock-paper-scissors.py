from random import randint

play_options = ['Rock', 'Paper', 'Scissors']

computer = play_options[randint(0,2)]

player = False

while player == False: 
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print("Tie!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("You lose!", computer, 'covers', player)
        else:
            print('You win!', player, 'crushes', computer)
    elif player == 'Paper':
        if computer == 'Scissors': 
            print('You lose!', computer, 'cuts', player)
        else:
            print('You win!', player, 'covers', computer)
    elif player == 'Scissors': 
        if computer == 'Rock':
            print('You lose!', computer, 'smashes', player)
        else:
            print('You win!', player, 'cuts', computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = play_options[randint(0,2)]
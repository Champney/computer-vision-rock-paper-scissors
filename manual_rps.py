
def get_computer_choice():
    selections = ['Rock', 'Paper', 'Scissors']
    import random
    x = random.choice(selections)
    #print(x)
    return x
    
def get_user_choice():
    x = input().capitalize()
    return x

def get_winner(computer_choice,user_choice):
    x = computer_choice
    y = user_choice
    if x == y:
        print("It is a tie!")
    elif y == 'Rock' and x == 'scissors':
        print("You won!")
    elif y == 'Scissors' and x == 'Paper':
        print("You won!")
    elif y == 'Paper' and x == 'Rock':
        print("You won!")
    elif x == 'Rock' and y == 'Scissors':
        print("You lost")
    elif x == 'Scissors' and y == 'Paper':
        print("You lost")
    elif x == 'Paper' and y == 'Rock':
        print("You lost")
def play():
    get_winner(get_user_choice(), get_computer_choice())
play()

selections = ['Rock', 'Paper', 'Scissors']
import random
def get_computer_choice():
    x = random.choice(selections).lower()
    #print(x)
    return x
    
def get_user_choice():
    return input().lower()

x = get_computer_choice()
y = get_user_choice()
if x == y:
    print("It's a draw")
elif y == 'rock' and x == 'scissors':
    print("You win")
elif y == 'scissors' and x == 'paper':
    print("You win")
elif y == 'paper' and x == 'rock':
    print("You win")
elif x == 'rock' and y == 'scissors':
    print("You lose")
elif x == 'scissors' and y == 'paper':
    print("You lose")
elif x == 'paper' and y == 'rock':
    print("You lose")
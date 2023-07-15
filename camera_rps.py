import time
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #This line and the one above it disable irrelevant warning messages
import cv2 
from keras.models import load_model
import numpy as np
model = load_model('./keras_model.h5',compile=False)
computer_wins = 0
user_wins = 0

def get_prediction():
    print('Determining your choice...')
    #countdown
    t = 3
    while t > 0:
        print(f"Countdown: {t}")
        t -= 1
        time_start = time.time()
        while (time.time() - time_start) < 1:
            pass

    while True: 
        prediction = get_image_from_webcam()
        
        #Assign the correct probability to the correct gesture
        if prediction[0][0] > 0.75:
            x = 'Scissors'
            break
        
        elif prediction[0][1] > 0.75:
            x = 'Rock'
            break

        elif prediction[0][2] > 0.75:
            x = 'Paper'
            break
        elif prediction[0][3] > 0.75:
            x = 'None'
    print(f"You chose {x}")
    return x

def get_computer_choice():
    selections = ['Rock', 'Paper', 'Scissors']
    import random
    x = random.choice(selections)
    return x

def get_winner(computer_choice,user_choice):
    global user_wins
    global computer_wins
    x = computer_choice
    y = user_choice
    
    print(f'Your choice: {y}, computer choice {x}')
    if x == y:
        print("It is a tie!")
        pass
    elif y == 'Rock' and x == 'Scissors':
        print("You won")
        user_wins += 1
        pass
    elif y == 'Scissors' and x == 'Paper':
        print("You won")
        user_wins += 1
        pass
    elif y == 'Paper' and x == 'Rock':
        print("You won")
        user_wins += 1
        pass
    elif x == 'Rock' and y == 'Scissors':
        print("You lost")
        computer_wins += 1
        pass
    elif x == 'Scissors' and y == 'Paper':
        print("You lost")
        computer_wins += 1
        pass
    elif x == 'Paper' and y == 'Rock':
        print("You lost")
        computer_wins += 1
        pass
    
def get_image_from_webcam():
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    cv2.imshow('frame', frame)
    prediction = model.predict(data, verbose=0)

    #release the cap object once the prediction variable is assigned
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction


    
def play():
    
    while computer_wins < 3 and user_wins < 3:
        get_winner(get_computer_choice(),get_prediction())
    if user_wins > 2:
        print("You win, well done")
    if computer_wins > 2:
        print("The computer beat you")
    
    
play()

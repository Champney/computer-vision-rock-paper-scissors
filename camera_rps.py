def get_prediction():
    import cv2 
    from keras.models import load_model
    import numpy as np
    model = load_model('./keras_model.h5',compile=False)
    with open('./labels.txt') as f:
        labels = [line.strip() for line in f.readlines()]
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose=0)

        cv2.imshow('frame', frame)
        #time.sleep(5)
        # Press q to close the window
        #print(prediction)
        if prediction[0][0] > 0.8:
            x = 'Scissors'
            return x
            
        elif prediction[0][1] > 0.8:
            x = 'Rock'
            return x
        elif prediction[0][2] > 0.8:
            x = 'Paper'
            return x
        elif prediction[0][3] > 0.8:
            x = 'None'
            return x
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
def get_computer_choice():
    selections = ['Rock', 'Paper', 'Scissors']
    import random
    x = random.choice(selections)
    return x

def get_winner(computer_choice,user_choice):
    x = computer_choice
    y = user_choice
    print(f'Your choice: {y}, computer choice {x}')
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
    get_winner(get_prediction(), get_computer_choice())
    
play()


from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import pandas as pd
import os
from datetime import datetime
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

# initialized values
img_width, img_height = 150, 150
input_shape = (img_width, img_height, 3)
test_model = load_model('model.h5')
basedir = "data2/test/"
i = 0
j = 0

# prediction function
def predict(basedir, i, j, model):
    if i == 0:
        basedir += "0/bike."
    elif i == 1:
        basedir += "1/motorcycle."
    elif i == 2:
        basedir += "2/car."

    path = basedir+str(j)+'.JPG'

    img = load_img(path, False, target_size=(img_width, img_height))

    x = img_to_array(img)
    x = x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict_classes(x)
    probs = model.predict_proba(x)

    if preds == 0:
        print('bicycle')
    if preds == 1:
        print('motorcycle')
    if preds == 2:
        print('car')

    print('')
    print('Probability: {}'.format(probs*100))

    return preds, probs


# Segment 6
# This is the main function. In this function, it iterates through all the test data and
# generates a prediction using the model.

score = 0
# bike, motor, car
car = [0, 0, 0]
motor = [0, 0, 0]
bike = [0, 0, 0]
for i in range(0, 3):
    for j in range(0, 110):  # Images to be tested

        print('Test Sample: ', j)

        (preds, probs) = predict(basedir, i, j, test_model)  # prediction

        if preds == 0:
            bike[i] += 1
        elif preds == 1:
            motor[i] += 1
        elif preds == 2:
            car[i] += 1

        if preds == i:
            score += 1

        print(' ')

print("Bike:\n-0: ", bike[0], "\n-1: ", bike[1], "\n-2: ", bike[2])
print("Motor:\n-0: ", motor[0], "\n-1: ", motor[1], "\n-2: ", motor[2])
print("Car:\n-0: ", car[0], "\n-1: ", car[1], "\n-2: ", car[2])
print("Score: ", score, "/ 330")
print("Accuracy: ", (score/330)*100)
# predict input
# write input into csv
# time log
# write checked in 1

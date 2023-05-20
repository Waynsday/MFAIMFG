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
basedir = "data2/input/"
entry = "data2/input"
count = 0


def fileCount():
    return [name for name in os.listdir(entry) if os.path.isfile(os.path.join(entry, name))]


# prediction function
def predict(basedir, i, model):

    path = basedir+i

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

    print('Probability: {}'.format(probs*100))

    return preds, probs


# Segment 6
# This is the main function. In this function, it iterates through all the test data and
# generates a prediction using the model.

column_names = ["Time In", "Time Out", "Vehicle Type", "Checked In"]

fname = 'Vehicle Log.csv'
if os.path.exists(fname):
    df = pd.read_csv(fname)
    print('[INFO] Opening File')
else:
    df = pd.DataFrame(columns=column_names)
    print('[INFO] File does not exist')
    print('[INFO] Generating ', fname)

files = fileCount()


for i in files:  # Images to be tested

    print('Entry {0}: {1} '.format(count, i))

    (preds, probs) = predict(basedir, i, test_model)  # prediction

    now = datetime.now()
    tempdata = [[now.strftime("%m/%d/%Y, %H:%M:%S"), " ", int(preds), 1]]
    tempdf = pd.DataFrame(tempdata, columns=column_names)
    df = df.append(tempdf, ignore_index=True)
    print(df)
    print(' ')
    count += 1

df.to_csv('Vehicle Log.csv', index=False)
# predict input
# write input into csv
# time log
# write checked in 1

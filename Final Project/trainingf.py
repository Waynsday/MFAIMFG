# Segment 1
# In this code segment, all the image processing libraries are imported
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K


# Segment 2
# In this code segment, we establish the parameters to be used for our training and validation
# including the directories to be used.
img_width, img_height = 150, 150

train_data_dir = 'data2/train'
validation_data_dir = 'data2/validation'
nb_train_samples = 1540
nb_validation_samples = 550
epochs = 20
batch_size = 16


# Segment 3
# This code segment specifies where the 'channels' are in the input data
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
    print("img data format channels_first")
else:
    input_shape = (img_width, img_height, 3)


# Segment 4
# This creates a sequential model and initializes a Convolutional Neural Network
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


# Segment 5
# Increased number of filters while reducing spatial dimensions
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


# Segment 6
# In this segment, the input layer is flatten to transform it into a flat array. Then the dense network
# creates the nodes. The relu is the activation function that would determine the output based a given
# set of input nodes. A dropout layer is added to avoid over fitting, then once again activated using a
# a softmax activation function.
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3))
model.add(Activation('softmax'))


# Segment 7
# Creates a python object that will build the CNN. The loss function to be used is
# categorical cross entropy with RMSprop as the optimizer.
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Segment 8
# Generates batches of image data for training
# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)


# Segment 9
# Generates batches of image data for testing
# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)


# Segment 10
# Generates batches of augmented and normalized data for training
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

print("train_generator")


# Segment 11
# Generates batches of augmented and normalized data for validation
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

print("validation_generator")


# Segment 12
# Fits the initialized model to identify the best values to map the input to the output
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

print("fit_generator")


# Segment 13
# Saves the optimized model and weights
model.save('model.h5')
model.save_weights('weights.h5')

print("Saved model and weights")

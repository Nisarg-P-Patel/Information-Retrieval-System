# -*- coding: utf-8 -*-
"""Information Retrieval from Multimedia Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Is9f-3tr93Wye5C_HpmLUvfvSdD23OF0

# AIM :- Information Retrieval from multimedia data.

To perfrom this practical we have choose topic of FOOD CLASSIFICATION

# Mouting drive to access the dataset
"""

from google.colab import drive
drive.mount("/content/MyDrive")

!cp "/content/MyDrive/My Drive/data.tar.gz" "data.tar.gz"

!tar -xzf "data.tar.gz"
!rm "data.tar.gz"

"""# Importing necessary libraries"""

import pandas as pd
import numpy as np
import os
import cv2
from keras.callbacks import Callback
from keras.backend import clear_session
from keras.models import Model, load_model
from keras.layers import Dense, Input, Flatten
from keras.applications import Xception

"""# Loading the images data"""

def load_data(df):

    trainX, testX, valX = [], [], []
    trainY, testY, valY = [], [], []

    for i in range(len(df)):

        item = df.loc[i][0]
        current_label = np.array((df.loc[i])[1:])

        path = os.path.join('data/keras/images', item)
        list_of_imgs = [os.path.join(path, file) for file in os.listdir(path)]
        train_set = list_of_imgs[:30]
        val_set = list_of_imgs[30:40]
        test_set = list_of_imgs[40:]

        for file in train_set:
            img = cv2.resize(cv2.cvtColor(cv2.imread(file, 1), cv2.COLOR_BGR2RGB), (224, 224))
            trainX.append(img)
            trainY.append(current_label)

        for file in val_set:
            img = cv2.resize(cv2.cvtColor(cv2.imread(file, 1), cv2.COLOR_BGR2RGB), (224, 224))
            valX.append(img)
            valY.append(current_label)

        for file in test_set:
            img = cv2.resize(cv2.cvtColor(cv2.imread(file, 1), cv2.COLOR_BGR2RGB), (224, 224))
            testX.append(img)
            testY.append(current_label)

    return (np.array(trainX), np.array(trainY), np.array(testX),
            np.array(testY), np.array(valX), np.array(valY))

print('Loading Data...')
df = pd.read_csv('data/keras/clean_anno_reduced.csv')
trainX, trainY, testX, testY, valX, valY = load_data(df)
print('Data Loaded.')

"""# Pre-processing the data (normalization)"""

trainX = trainX.astype(np.float32)
testX = testX.astype(np.float32)
valX = valX.astype(np.float32)

trainY = trainY.astype(np.float32)
testY = testY.astype(np.float32)
valY = valY.astype(np.float32)

MEAN = np.mean(trainX, axis = (0,1,2))
STD = np.std(trainX, axis = (0,1,2))

for i in range(3):
    trainX[:, :, :, i] = (trainX[:, :, :, i] - MEAN[i]) / STD[i]
    testX[:, :, :, i] = (testX[:, :, :, i] - MEAN[i]) / STD[i]
    valX[:, :, :, i] = (valX[:, :, :, i] - MEAN[i]) / STD[i]

"""# Using Xception model for classification"""

img = Input(shape = (224, 224, 3))
model = Xception(include_top=False,
                            weights='imagenet',
                            input_tensor=img,
                            pooling='avg')

"""# Training the model"""

final_layer = model.layers[-1].output

dense_layer_1 = Dense(128, activation = 'relu')(final_layer)
output_layer = Dense(10, activation = 'sigmoid')(dense_layer_1)

model = Model(inputs = img, outputs = output_layer)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy' , metrics = ['accuracy'])
model.fit(trainX, trainY, batch_size = 32, epochs = 25, validation_data = (valX, valY))

"""# Saving weights for future usage"""

model.save_weights("model.h5")

cp "model.h5" '/content/MyDrive/My Drive/multilabel'

"""# Visualization of loss"""

from matplotlib import pyplot as plt
loss_train = model.history.history['loss']
loss_val = model.history.history['val_loss']
epochs = range(1,26)
plt.plot(epochs, loss_train, 'g', label='Training loss')
plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

"""# For Testing Purpose"""

from google.colab import drive
drive.mount("/content/MyDrive")

"""# Assigning the trained weights to the same model used for training for testing"""

img = Input(shape = (224, 224, 3))
model = Xception(include_top=False,
                            weights='imagenet',
                            input_tensor=img,
                            pooling='avg')

final_layer = model.layers[-1].output

dense_layer_1 = Dense(128, activation = 'relu')(final_layer)
output_layer = Dense(10, activation = 'sigmoid')(dense_layer_1)

model = Model(inputs = img, outputs = output_layer)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy' , metrics = ['accuracy'])
model.load_weights("/content/MyDrive/My Drive/multilabel/model.h5")

"""# Uploading images for checking"""

from google.colab import files
uploaded = files.upload()

labels = ['healthy','junk','dessert','appetizer','mains','soups','carbs','protein','fats','meat']

"""# Output of the model"""

filename = uploaded.keys()
from matplotlib import pyplot as plt
for i in filename:
    img = cv2.resize(cv2.cvtColor(cv2.imread(i, 1), cv2.COLOR_BGR2RGB), (224, 224))
    plt.imshow(img)
    plt.show()
    img = img.reshape(-1,224,224,3)
    prediction = model.predict(img)
    for i in range(10):
        print(labels[i],prediction[0][i]*100,"%")

"""# Learning outcomes

1. I got to learn how the Information can be retrieved from images data also.
2. I got to learn how we can apply advanced techniques like ML-DL algorithms for the same purpose.
3. I got to learn how we can use image data for various purposes.
"""

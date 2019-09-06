# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:51:06 2019

@author: north_ner
"""

import tensorflow as tf
from tensorflow import keras
(train_images,train_lables),(test_images,test_lables)=keras.datasets.mnist.load_data()

model=keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation=tf.nn.softmax)
        ])


model.compile(optimizer=tf.compat.v1.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_images,train_lables,epochs=5)


test_loss,test_acc=model.evaluate(test_images,test_lables)
print('test accuracy=',test_acc)
#z=open('3.jpg','r')
prediction=model.predict(test_images)
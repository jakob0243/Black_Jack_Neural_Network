#import tensorflow as tf
import tensorflow.keras.models as tf

import numpy as np

model = tf.load_model("testingtesting.model")

CATEGORIES = []

while True:
    p1 = int(input("player card 1: "))
    p2 = int(input("player card 2: "))
    d1 = int(input("Dealer card 1: "))
    arra = [[p1, p2, d1]]
    arra = np.array(arra)
    print(arra)
    prediction = model.predict(arra)
    print(prediction)
    print(prediction[0][0] // 1)
    #print(prediction[0])
    #result = np.where(prediction[0] == max(prediction[0]))
    #print(result[0][0])
    #print(CATEGORIES[result[0][0]])
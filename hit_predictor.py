'''
A Neural Network for predicting whether you should hit or stand 
in a game of black jack given you cards and the known card of the 
Dealer
Jakob Mckinney
09/07/2019
'''
import tensorflow.keras.models as tf
import numpy as np

model = tf.load_model("testingtesting.model")

CATEGORIES = ["HIT", "STAND"]

while True:
    # Asks for the cards of the player and the card of the dealer
    p1 = int(input("player card 1: "))
    p2 = int(input("player card 2: "))
    d1 = int(input("Dealer card 1: "))
    # Adds these to a numpy array to use as input
    arra = [[p1, p2, d1]]
    arra = np.array(arra)
    print(arra)
    # Uses model to make a prediction on the given input and prints it
    prediction = model.predict(arra)
    print(prediction)
    print(CATEGORIES[int(prediction[0][0] // 1)])
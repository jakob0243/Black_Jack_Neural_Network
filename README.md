# Black_Jack_NN

Basic Neural Network using tensorflow, trained on 900,000 hands of black jack (https://www.kaggle.com/mojocolors/900000-hands-of-blackjack-results)

Data in Hit_Data.rar has been changed from the original .csv to only included the need values.

TraingDataHits.ipynb Takes the .csv file, Hit_Data.rar, and puts the relevant values into a Features list and a Labels list,
shuffles them and then they are stored in X.pickle (Features) and y.pickle (Labels).

HitsModel.ipynb creates the neural network model using tensorflow and loads in the data from X.pickle and y.pickle, it then
compiles the model and trains it on the data (X.pickle, y.pickle). Once it is trained the model is saved.

hit_predictor.py is a program that loads in the trained model and then asks the user what two cards they have and what card
the dealer is showing, it then uses the model the model to predict whether the user should hit and stand.
  -The model should be given an integer corresponding to the in game value of the card, e.g. king: 10, ace: 1 or 11, 8: 8, etc...
  
 Dependencies:
  -Tensorflow (Keras aswell)
  -Pickle
  -Numpy
  -Random

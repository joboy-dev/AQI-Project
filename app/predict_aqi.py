import pickle
import numpy as np
import sklearn

with open('ML/model.pickle', mode='rb') as model_file:
    model = pickle.load(model_file)
    

def predict_aqi(temperature, pressure, humidity, wind):
    '''Function to use model to predict AQI'''
    
    X_test = np.array([[temperature, pressure, humidity, wind]])
    
    y_pred = model.predict(X_test)
    return y_pred
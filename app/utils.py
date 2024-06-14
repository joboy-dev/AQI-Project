import pickle
import numpy as np
import sklearn
    

def predict_aqi(temperature, pressure, humidity, wind):
    '''Function to use model to predict AQI'''
    
    with open('ML/model.pickle', mode='rb') as model_file:
        model = pickle.load(model_file)
    
    X_test = np.array([[temperature, pressure, humidity, wind]])
    
    y_pred = model.predict(X_test)
    return y_pred


def get_aqi_recommendation(aqi):
    '''Function to get recommendations on Air Quality'''
    
    if aqi >= 0.0 and aqi <= 50.0:
        return {
            'Air Pollution Level': 'Good',
            'Health Implications': 'Air quality is considered satisfactory, and air pollution poses little or no risk',
            'Cautionary Statement': 'None'
        }
        
    elif aqi >= 51.0 and aqi <= 100.0:
        return {
            'Air Pollution Level': 'Moderate',
            'Health Implications': 'Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution',
            'Cautionary Statement': 'Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion'
        }
        
    elif aqi >= 101.0 and aqi <= 150.0:
        return {
            'Air Pollution Level': 'Unhealthy for sensitive groups',
            'Health Implications': 'Members of sensitive groups may experience health effects. The general public is not likely to be affected',
            'Cautionary Statement': 'Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion'
        }
        
    elif aqi >= 151.0 and aqi <= 200.0:
        return {
            'Air Pollution Level': 'Unhealthy',
            'Health Implications': 'Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects',
            'Cautionary Statement': 'Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion'
        }
        
    elif aqi >= 201.0 and aqi <= 300.0:
        return {
            'Air Pollution Level': 'Very unhealthy',
            'Health Implications': 'Health warnings of emergency conditions. The entire population is more likely to be affected',
            'Cautionary Statement': 'Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion'
        }
    
    else:
        return {
            'Air Pollution Level': 'Hazardous',
            'Health Implications': 'Health alert: everyone may experience more serious health effects',
            'Cautionary Statement': 'Everyone should avoid all outdoor exertion'
        }

    
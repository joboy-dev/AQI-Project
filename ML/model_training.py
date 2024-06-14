import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import pickle

def clean_data():
    '''Function to clean csv data'''
    
    # Load csv data
    print('Reading csv...')
    df = pd.read_csv('data/aqi_data.csv')
    
    print('Cleaning data...')
    
    # Remove time column as it won't be useful in the long run
    df.drop(columns=['date', 'time'], axis=1, inplace=True)
    
    # Remove duplocate values from csv data
    df.drop_duplicates(inplace=True)
    
    # TODO: Drop null values if need be
        
    return df


if __name__ == '__main__':
    '''Train and retrain the model'''
    
    print('Loading cleaned data...')
    clean_df = clean_data()
    
    print(clean_df)
    print('Splitting data into train and test data...')
    
    # Get independent variables
    X = clean_df.drop(columns=['pm25'])
    y = clean_df['pm25'] 
    
    # Split data set into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
    
    print('Setting up model...')
    lreg = LinearRegression()
    
    print('Training model...')
    lreg.fit(X_train, y_train)
    y_pred = lreg.predict(X_test)
    
    print('Getting accuracy score...')
    
    print(f'R2 Score: {metrics.r2_score(y_test, y_pred)}')
    print(f'RMSE: {metrics.mean_squared_error(y_test, y_pred)}')
    
    print('Saving model...')
    with open('ML/model.pickle', mode='wb') as file:
        pickle.dump(lreg, file)
    
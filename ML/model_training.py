import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn import metrics

def clean_data():
    '''Function to clean csv data'''
    
    # Load csv data
    df = pd.read_csv('data/aqi_data.csv')
    
    # Remove time column as it won't be useful in the long run
    df.drop(columns=['date', 'time'], axis=1, inplace=True)
    
    # Remove duplocate values from csv data
    df.drop_duplicates(inplace=True)
    
    # TODO: Drop null values if need be
    
    print(df)
    
    return df


def train_model():
    '''Function to train and retrain the model'''
    
    clean_df = clean_data()
    
    
    
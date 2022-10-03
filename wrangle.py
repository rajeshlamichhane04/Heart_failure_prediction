#import data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



def split_data(df):
    #split data in train_val, test
    train_val,test = train_test_split(df, test_size = 0.2, stratify = df.death_event, random_state = 123)
    #split data into train, validate
    train,validate = train_test_split(train_val, test_size = 0.3, stratify = train_val.death_event, random_state = 123)
    return train,validate,test


def nulls_by_col(df):
    #add nulls by row
    num_rows_missing = df.isnull().sum()
    #get percentt null
    pct_rows_missing = df.isnull().sum() / df.shape[0] * 100
    cols_missing = pd.DataFrame({
        "num_rows_missing" : num_rows_missing ,
        " pct_rows_missing" : pct_rows_missing
    })
    return cols_missing


def nulls_by_rows(df):
    #get null by column
    num_missing = df.isnull().sum(axis =1)
    #get null percent by column
    pct_missing = (num_missing / df.shape[1]) * 100
    missing_values = pd.DataFrame({"num_missing":num_missing, "pct_missing":pct_missing})\
                    .reset_index().groupby(["num_missing","pct_missing"]).count()\
    .rename(index=str, columns={'index': 'num_rows'}).reset_index()
    return missing_values


def handle_missing_values(df,prop_required_columns,prop_required_row):
    #define threshold
    threshold = int(round(prop_required_columns * len(df.index),0))
    #drop null at thesholf
    df = df.dropna(axis = 1 , thresh = threshold)
    threshold = int(round(prop_required_row * len(df.columns),0 ))
    df = df.dropna(axis = 0, thresh = threshold)
    return df




def remove_outliers(df, k, col_list):
    for col in col_list:
         #get the 1st and 3rd quantiles
        q1, q3 = df[col].quantile([.25, .75]) 
         # calculate interquartile range
        iqr = q3 - q1   
         # get upper bound
        upper_bound = q3 + k * iqr   
          # get lower bound
        lower_bound = q1 - k * iqr   
         # dataframe without outliers
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        return dfc
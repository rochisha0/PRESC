# importing required dependencies 
from IPython.display import HTML 
from tabulate import tabulate
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns

# read data file
address = "../../datasets/eeg.csv"
df = pd.DataFrame(pd.read_csv(address))
    
def data_info():
    '''
    Displays basic information about a dataset :
		first 5 rows of dataset
		last 5 rows of dataset
		info of each column of dataset
		description on the dataset
		sum of all null values in a dataset for preprocessing
    '''
    print("\nFirst 5 rows of datasets: ")
    display(df.head(5)) 
    print("\nLast 5 rows of datasets: ")
    display(df.tail(5))
    print("\nDescription of each column: \n")
    display(df.describe())   
    print("\nInformation of each column: \n")
    display(df.info()) 
    print("\nChecking for null values: \n")
    print(df.isnull().sum())   


def data_visuals():
	'''
	Visualises basic infromation about the dataset.
	This function is specific to the eeg dataset.
	'''
    df.Class.unique()
    sns.countplot(df.Class)

# splitting the data 
def train_test_split_data(test_size):
	'''
	Splits the data into 2 portions, training and testing.
	
	Parameters:
		test_size : float-range(0,1), the ratio of test size to total size.

	Returns:
		X_train : array-like, shape(n_train_samples, n_features)
		X_test : array-like, shape(n_test_samples, n_features)
		y_train : of length n_train_samples
		y_test : of length n_test_samples
	'''
    y = df.Class
    X = df.drop('Class',axis = 1)
    random_state = 40
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)

    return X_train, X_test,y_train, y_test

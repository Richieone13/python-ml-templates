# Data Preprocessing
# 13/07/2019 - If libarires are not working or not found it is likely the libaries are updated.

# This template is borrowed from A-Z Machine Learning Course oN Udemy.

# Importing the libraries
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv') #Panda Library - Checking out file to see NaN values
X = dataset.iloc[:, :-1].values #Setting X for all columns except the last one (iloc)
y = dataset.iloc[:, 3].values #Select the specific column to set y

# Taking care of missing data
from sklearn.impute import SimpleImputer #Importing library to sort out missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean') #Command + I to show how to use method
X[:, 1:3] = imputer.fit_transform(X[:, 1:3]) #Transform the data by filling in NaN

# Encoding categorical data - For machine learning purposes
# Encoding X categorical data + HotEncoding
from sklearn.preprocessing import  OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float) #Typing in X in the IPython Console to check if object

# Encoding Y data (Independent Variable)
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)

#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split #Check if these modules change
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =0)

#Feature Scaling - this is great to speed up the algorithms Converge faster - known as 'Euclidean Distance between two points
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #Both scale on the same basis
#y_test and y_train don't require future scaling because it is a classification problem and has a binary output
 
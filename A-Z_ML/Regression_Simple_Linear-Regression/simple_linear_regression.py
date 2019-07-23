# Simple Linear Regression
# For Salary and Years of Experience

# Importing the libraries
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split #Check if these modules change
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state =0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression().fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set result
plt.figure(1)

plt.scatter(X_train, y_train, color = 'red') #Red line is the actuals
plt.plot(X_train, regressor.predict(X_train), color = 'blue') #Blue line is the predicted values
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.savefig('Linear_Regression-train.png')

# Visualising the Test set results
plt.figure(2)

plt.scatter(X_test, y_test, color = 'green') #Red line is the actuals
plt.plot(X_train, regressor.predict(X_train), color = 'blue') #Blue line is the predicted values
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.savefig('Linear_Regression-test.png')


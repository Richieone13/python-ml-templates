# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2:3].values # Changed this code as got error - Expected 2D array, got 1D array instead

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting the SVR Model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf') # non linear
regressor.fit(X, y)

# Predicting a new result
y_pred = regressor.predict(np.array(6.5).reshape(1,-1)) # without feature scaling 13,000
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array(6.5).reshape(1,-1)))) 
#or
# y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array[[6.5]]))) 
# apply to transform back, inversing the answer for y and apply the transform for X parameters

"""
# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
"""

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
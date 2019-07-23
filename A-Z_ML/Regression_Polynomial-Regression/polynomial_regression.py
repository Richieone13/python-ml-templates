# Polynoimal Regression
# Bluffing Regression model

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv') # Non Linear Relationship
X = dataset.iloc[:, 1:-1].values # Matrix 10, 1
y = dataset.iloc[:, 2].values # This is a vector

# Splitting the dataset into the Training set and Test set
# Not enough data so not required to do train test split.
"""from sklearn.model_selection import train_test_split #Check if these modules change
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =0)"""

# No need to input feature scaling

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =2  ) #Create object of this class
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results - More continuous curve with X_grid
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
print(lin_reg.predict(np.array(6.5).reshape(1,-1)))

# Predicting a new result with Polynomial Regression
print(lin_reg_2.predict(poly_reg.fit_transform(np.array(6.5).reshape(1,-1))))
import numpy as np
import matplotlib.pyplot as plt

# Generating sample dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

# Calculating the coefficients (slope and intercept) of the best-fitting line
slope, intercept = np.polyfit(X, Y, 1)

# Predicting Y values based on the model
predicted_Y = slope * X + intercept

# Calculating the Mean Squared Error (MSE)
mse = np.mean((Y - predicted_Y) ** 2)

# Calculating the Coefficient of Determination (R^2 score)
ss_residual = np.sum((Y - predicted_Y) ** 2)
ss_total = np.sum((Y - np.mean(Y)) ** 2)
r_squared = 1 - (ss_residual / ss_total)

# Printing the results
print("Mean Squared Error (MSE):", mse)
print("Coefficient of Determination (R^2 score):", r_squared)

# Plotting the original data and the best-fitting line
plt.scatter(X, Y, label='Original Data')
plt.plot(X, predicted_Y, color='red', label='Best-Fitting Line')
plt.xlabel('X (Independent Variable)')
plt.ylabel('Y (Dependent Variable)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

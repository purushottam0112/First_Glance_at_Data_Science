# write your code here
########################### Stage 1/4: Fit method #################################
import numpy as np

class CustomLinearRegression:
    def __init__(self, *, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        beta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)
        self.intercept = beta[0]
        self.coefficient = beta[1:]


def main():
    x = [4.0, 4.5, 5, 5.5, 6.0, 6.5, 7.0]
    y = [33, 42, 45, 51, 53, 61, 62]

    linear_regression = CustomLinearRegression()
    linear_regression.fit(np.array([[1, x] for x in x]), y)
    print({'Intercept': linear_regression.intercept, 'Coefficient': linear_regression.coefficient})

main()
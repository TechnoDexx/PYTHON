# coding=utf-8
# Linear Regression Realization (http://dataaspirant.com/2014/12/20/linear-regression-implementation-in-python/)

# input_data.csv:
# square_feet;price
# 150;6450
# 200;7450
# 250;8450
# 300;9450
# 350;11450
# 400;15450
# 600;18450

# Required Packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name, sep=";")
    x_parameter = []
    y_parameter = []
    # TODO: Replace the names of the fields 'square foot', 'price' for your own values
    for single_square_feet in data['square_feet']:
        x_parameter.append([float(single_square_feet)])

    for single_price_value in data['price']:
        y_parameter.append(float(single_price_value))
    return x_parameter, y_parameter


# Function for Fitting our data to Linear model
# noinspection PyPep8Naming
def linear_model_main(x_parameters, y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(x_parameters, y_parameters)
    # noinspection PyArgumentList
    predict_outcome = regr.predict(predict_value)
    predictions = {'intercept': regr.intercept_, 'coefficient': regr.coef_, 'predicted_value': predict_outcome}
    return predictions


# Function to show the resutls of linear fit model
def show_linear_line(x_parameters, y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(x_parameters, y_parameters)
    plt.scatter(x_parameters, y_parameters, color='blue')
    # noinspection PyArgumentList
    plt.plot(x_parameters, regr.predict(x_parameters), color='red', linewidth=4)
    # Supress axis value
    plt.xticks(())
    plt.yticks(())
    plt.show()


X, Y = get_data('input_data.csv')
predicted_value = 700
result = linear_model_main(X, Y, predicted_value)
print('Constant Value: {0}'.format(result['intercept']))
print('Coefficient: {0}'.format(result['coefficient']))
print('Predicted Value: {0}'.format(result['predicted_value']))
show_linear_line(X, Y)
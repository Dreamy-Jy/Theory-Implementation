'''
This is an implementation of the Linear Regression Machine Learning Algorithm using
gradient descent to learn the parameters.
'''
import csv

# get the data set from a csv file
data_set_file = open("crickets.csv", newline='')
data_set = csv.reader(data_set_file)
# TODO: figure out how to remove headers from a data file

x_values = []
y_values = []

# the try statement is used to disregard
# string headers failing to convert to floats
for data in data_set:
    try:
        x_values.append(float(data[1]))
        y_values.append(float(data[0]))
    except:
        pass

data_set_file.close()


def make_predictions(training_x, slope, intercept):
    '''make predicts training data labels given the current value of the bias and weights'''
    return [(value *slope -intercept) for value in training_x]


def loss_function_partial_derivative(errors, training_x = None, is_bias = False):
    '''returns the partial derivative of the loss functions for weights and biases'''
    if is_bias == False and training_x == None:
        pass # throw error stating weights need a feature set
    elif is_bias:
        return sum(errors) /len(errors)
    else:
        return sum([ errors[i] *training_x[i] for i in range(len(errors)) ]) /len(errors)


# use object
def linear_regression_gradient_descent(training_x, training_y, learning_rate, learning_cycles):
    slope = 0.0
    intercept = 0.0
    predictions = []

    for _ in range(learning_cycles):
        # print("on run", _, "\n\tslope= ", slope, "\n\tintercept= ", intercept)
        predictions = make_predictions(training_x, slope, intercept)
        errors = [ (predictions[i] -training_y[i]) for i in range(len(training_y)) ]
        temp1 = slope -(learning_rate *loss_function_partial_derivative(errors, training_x = training_x)) 
        temp2 = intercept -((learning_rate) *loss_function_partial_derivative(errors, is_bias = True))
        # if _%20 == 0:
            # print("\nThese are the errors: ", errors, "\n\n\tThis is there sum: ", sum(errors), "\n\tThis is the intercept: ", intercept, "\n\n")
        # print("\tnew intercept= ",temp2)
        slope = temp1
        intercept = temp2 

    return [intercept, slope]


results = linear_regression_gradient_descent(x_values, y_values, 0.0003, 400000)
print("This is my slope ", results[1])
print("This is my y-intercept", results[0])

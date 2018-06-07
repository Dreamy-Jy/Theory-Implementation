'''
This is an implementation of the Linear Regression Machine Learning Algorithm using the
ordinary least of squares method.

Before I can start this algorithm I need to to:
!. find a good data set for simple OLS [x]
2. know the libraries I'm using []
    a. 
    b. 
    c. 
    d. 
3. learn the libraries I'm using
4. implement the algorithm

1 use data set

find m
'''
import csv

# get the data set for a csv file
data_set_file = open("crickets.csv", newline='')
data_set = csv.reader(data_set_file)
# figure out how to remove headers from a data file

x_values = []
y_values = []

# the try statement is used to disregard the
# headers failing to convert to floats
for data in data_set:
    try:
        x_values.append(float(data[1]))
        y_values.append(float(data[0]))
    except:
        pass

data_set_file.close()

# init and set weights using the ordinary
# least of squares method
m = 0
b = 0

x_mean = sum(x_values) /len(x_values)
y_mean = sum(y_values) /len(y_values)

num = 0
den = 0

for i in range(min(len(x_values), len(y_values))):
    num += (x_values[i] -x_mean) *(y_values[i] -y_mean)
    den += (x_values[i] -x_mean)**2

m = num /den
b = y_mean -(m *x_mean)

print("This is my slope ", m)
print("This is my y-intercept", b)

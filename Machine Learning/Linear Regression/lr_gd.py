import numpy as np

def computeErrorForLineGivenPoints(b, m, points):
    '''This function computes the error of a linear function'''
    totalError = 0
    for i in range(0, len(points)):
        y = points[i, 0]
        x = points[i, 1]
        totalError += (y -(m *x +b)) **2 # GOOGLE: how numpy arrays work
    return totalError /float(len(points)) # GOOGLE: how divson works in python 3

def stepGradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))

    for i in range(0, len(points)): # What does this loop do?
        y = points[i, 0]
        x = points[i, 1]
        b_gradient += -(2/N) *(y -(m_current *x +b_current))
        m_gradient += -(2/N) *x *(y -(m_current *x +b_current))
    
    new_b = b_current -(learningRate *b_gradient)
    new_m = m_current -(learningRate *m_gradient)
    return [new_b, new_m]

# A learning system that knows what it doesn't know
def funcname(parameter_list):
    pass

def run():
    pass

if __name__ == '__main__':
    run()

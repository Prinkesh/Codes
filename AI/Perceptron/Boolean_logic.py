#!/usr/bin/env python
#######################################################################################################################
### Author : Prinkesh Sharma                                                                                        ###
#######################################################################################################################
### LIBRARIES NEEDED numpy , pylab (matplotlib)                                                                     ###
###                                                                                                                 ###
###                                                                                                                 ###
### A Perceptron classifier to simulate Boolean Logic ,                                                             ###
### All linearly seperable Boolean logics can be simulated by this perceptron depending upon the training data      ###
### training data used here is for simulating AND Boolean Logic                                                     ###
#######################################################################################################################

from pylab import * # For plotting the error during Training Phase
from random import choice # For randomly choosing a data from training_data
from numpy import array, dot, random ###For enhancing array operations like dot product

unit_step = lambda x: 0 if x < 0 else 1 # Step Function or Activation Function

#Training Data to simulate 2 Input Boolean AND logic 
training_data = [ (array([0,0,1]),0),
                  (array([0,1,1]),1),
                  (array([1,0,1]),1),
                  (array([1,1,1]),0)
                ]


w = random.rand(3) #Intial Weight Vector
# Each of the element in the weight vector is in the range (0,1)

# For this case 'w' will look like:
###
#  array([ 0.34630468,  0.41118564,  0.21630602])
###

errors = [] # Error between expected result and the obtained result is stored in this list for each learning iteration

eta = 0.2 # Learinig Rate
n = 150 # No of Training Iteration

###Training Phase Starts with randomly choosen w for eacch input as well as dummy input

###                                 NOTE :
### ----------------------------------------------------------------------------------
### | Variable  |   Type      |    Example                                           |
### ----------------------------------------------------------------------------------
### | w         |   vector    |     array([ 0.34630468,  0.41118564,  0.21630602])   |
### | x         |   vector    |     array([ 0,  1,  1])                              |
### | eta       |   scalar    |     0.2                                              |
### | error     |   scalar    |     -1 to 1                                          |
### | expected  |   scalar    |     The expected result for the input                |
### ----------------------------------------------------------------------------------



for i in xrange(n):
    x, expected = choice(training_data) # A random data choosen from the training data set
    result = dot(w, x) # Dot Product of w and x 
    error = expected - unit_step(result) # Error Calcutation
    errors.append(error)
    w += eta * error * x # Weight Adjustment

### Final Results for input data calcuated by the trained perceptron
for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

### Code for Plotting the Training Phase Analysis Graph
    
xlabel('Number of Training Iteration(s)')
ylabel('Error')
title('Training Phase Analysis')
grid(True)
ylim([-1,1])
plot(errors)
savefig("test.png")
show()

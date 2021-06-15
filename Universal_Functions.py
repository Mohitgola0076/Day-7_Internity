'''
Universal functions in Numpy are simple mathematical functions. It is just a term that we gave to mathematical functions in the Numpy library. Numpy provides various universal functions that cover a wide variety of operations.
'''

                # Trigonometric functions:

# Python code to demonstrate trignometric function
import numpy as np

# create an array of angles
angles = np.array([0, 30, 45, 60, 90, 180])

# conversion of degree into radians
# using deg2rad function
radians = np.deg2rad(angles)

# sine of angles
print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))

# inverse sine of sine values
print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))

# hyperbolic sine of angles
print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))

# inverse sine hyperbolic
print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value))

# hypot function demonstration
base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height))


            # Output:
Sine of angles in the array:
[  0.00000000e+00   5.00000000e-01   7.07106781e-01   8.66025404e-01
   1.00000000e+00   1.22464680e-16]

Inverse Sine of sine values:
[  0.00000000e+00   3.00000000e+01   4.50000000e+01   6.00000000e+01
   9.00000000e+01   7.01670930e-15]

Sine hyperbolic of angles in the array:
[  0.           0.54785347   0.86867096   1.24936705   2.3012989
  11.54873936]

Inverse Sine hyperbolic:
[ 0.          0.52085606  0.76347126  0.94878485  0.74483916 -0.85086591]

hypotenuse of right triangle is:
5.0


                # Statistical functions:

# Python code demonstrate statistical function
import numpy as np

# construct a weight array
weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])

# minimum and maximum
print('Minimum and maximum weight of the students: ')
print(np.amin(weight), np.amax(weight))

# range of weight i.e. max weight-min weight
print('Range of the weight of the students: ')
print(np.ptp(weight))

# percentile
print('Weight below which 70 % student fall: ')
print(np.percentile(weight, 70))

# mean
print('Mean weight of the students: ')
print(np.mean(weight))

# median
print('Median weight of the students: ')
print(np.median(weight))

# standard deviation
print('Standard deviation of weight of the students: ')
print(np.std(weight))

# variance
print('Variance of weight of the students: ')
print(np.var(weight))

# average
print('Average weight of the students: ')
print(np.average(weight))


            # Output:
    
Minimum and maximum weight of the students: 
45.0 73.25

Range of the weight of the students: 
28.25

Weight below which 70 % student fall: 
55.317

Mean weight of the students: 
54.3225

Median weight of the students: 
51.6

Standard deviation of weight of the students: 
8.05277397857

Variance of weight of the students: 
64.84716875

Average weight of the students: 
54.3225

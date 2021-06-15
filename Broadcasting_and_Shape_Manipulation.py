'''
The term broadcasting refers to how numpy treats arrays with different Dimension during arithmetic operations which lead to certain constraints, the smaller array is broadcast across the larger array so that they have compatible shapes. 
'''
            # Example

import numpy as np

A = np.array([5, 7, 3, 1])
B = np.array([90, 50, 0, 30])

# array are compatible because of same Dimension
c = a * b
print (c)


            # Example : 
    
macros = array([
[0.8, 2.9, 3.9],
[52.4, 23.6, 36.5],
[55.2, 31.7, 23.9],
[14.4, 11, 4.9]
])

# Create a new array filled with zeros,
# of the same shape as macros.
result = zeros_like(macros)

cal_per_macro = array([3, 3, 8])

# Now multiply each row of macros by
# cal_per_macro. In Numpy, `*` is
# element-wise multiplication between two arrays.
for i in range(macros.shape[0]):
	result[i, :] = macros[i, :] * cal_per_macro

result

        # Output : 

array([[   2.4,    8.7,   31.2 ],
       [  157.2,   70.8,  292 ],
       [   165.6,  95.1,   191.2],
       [   43.2,   33,    39.2]])


                # Single Dimension array 

import numpy as np
a = np.array([17, 11, 19]) # 1x3 Dimension array
print(a)
b = 3
print(b)

# Broadcasting happened because of
# miss match in array Dimension.
c = a + b
print(c)

            # Output: 
 
[17 11 19]
3
[20 14 22]



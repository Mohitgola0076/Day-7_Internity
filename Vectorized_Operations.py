'''
The concept of vectorized operations on NumPy allows the use of more optimal and pre-compiled functions and mathematical operations on NumPy array objects and data sequences. The Output and Operations will speed-up when compared to simple non-vectorized operations.
'''

                # Example

# importing the modules
import numpy as np
import timeit

# vectorized sum
print(np.sum(np.arange(15000)))

print("Time taken by vectorized sum : ", end = "")
%timeit np.sum(np.arange(15000))

# itersative sum
total = 0
for item in range(0, 15000):
	total += item
a = total
print("\n" + str(a))

print("Time taken by iterative sum : ", end = "")
%timeit a

                
                # Example 

# importing the modules
import numpy as np
import timeit
import math

# vectorized operation
print("Time taken by vectorized operation : ", end = "")
%timeit np.exp(np.arange(150))

# non-vectorized operation
print("Time taken by non-vectorized operation : ", end = "")
%timeit [math.exp(item) for item in range(150)]



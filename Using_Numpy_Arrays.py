'''
The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.
One can find:

rank, determinant, trace, etc. of an array.
eigen values of matrices
matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
solve linear or tensor equations and much more!
'''

            # Example 1 
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))


        # Output:

Rank of A: 3

Trace of A: 11

Determinant of A: -306.0

Inverse of A:
 [[ 0.17647059 -0.00326797 -0.02287582]
 [ 0.05882353 -0.13071895  0.08496732]
 [-0.11764706  0.1503268   0.05228758]]

Matrix A raised to power 3:
 [[336 162 228]
 [406 162 469]
 [698 702 905]]


            # Matrix eigenvalues Functions
    
# Python program explaining eigh() function
 
from numpy import linalg as geek
 
# Creating an array using array 
# function
a = np.array([[1, -2j], [2j, 5]])
 
print("Array is :",a)
 
# calculating an eigen value
# using eigh() function
c, d = geek.eigh(a)
 
print("Eigen value is :", c)
print("Eigen value is :", d)

           # Output :

Array is : [[ 1.+0.j,  0.-2.j],
                [ 0.+2.j,  5.+0.j]]

Eigen value is : [ 0.17157288,  5.82842712]

Eigen value is : [[-0.92387953+0.j , -0.38268343+0.j ],
       [ 0.00000000+0.38268343j,  0.00000000-0.92387953j]]


                # Matrix and vector products
    
# Python Program illustrating
# numpy.dot() method
 
import numpy as geek
 
# Scalars
product = geek.dot(5, 4)
print("Dot Product of scalar values  : ", product)
 
# 1D array
vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = geek.dot(vector_a, vector_b)
print("Dot Product  : ", product)


        # Output:

Dot Product of scalar values  :  20
Dot Product  :  (-7+22j)
    
    

        # A boolean mask

'''
Indexing and slicing are quite handy and powerful in NumPy, but with the booling mask it gets even better! Let's start by creating a boolean array first. Note that there is a special kind of array in NumPy named a masked array. Here, we are not talking about it but we're also going to explain how to extend indexing and slicing with NumPy
'''

 # Arrays:

In [58]: x = np.array([1,3,-1, 5, 7, -1]) 
In [59]: mask = (x < 0) 
In [60]: mask 
Out[60]: array([False, False,  True, False, False,  True], dtype=bool) 

'''
We can see from the preceding example that by applying the < logic sign that we applied scalars to a NumPy Array and the naming of a new array to mask, it's still vectorized and returns the True/False boolean with the same shape of the variable x indicated which element in x meet the criteria:
'''

In [61]: x [mask] = 0 
In [62]: x 
Out[62]: array([1, 3, 0, 5, 7, 0]) 
Using the mask, we gain the ability to access or replace any element value in our...


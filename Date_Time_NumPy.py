'''
With the help of numpy.datetime64() method, we can get the date in a numpy array in a particular format i.e year-month-day by using numpy.datetime64() method.
Syntax : numpy.datetime64(date)
Return : Return the date in a format ‘yyyy-mm-dd’.
'''

                # Example

# import numpy
import numpy as np

# using numpy.datetime64() method
gfg = np.array(np.datetime64('2019-08-26'))

print(gfg)

        # Output : 

array(‘2019-08-26′, dtype=’datetime64[D]’)

                # Example

# import numpy
import numpy as np

# using numpy.datetime64() method
gfg = np.array(np.datetime64('2019-08', 'D'))

print(gfg)

        # Output : 
    
array(‘2019-08-01′, dtype=’datetime64[D]’)

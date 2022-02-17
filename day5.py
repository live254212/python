"""n=5
for i in range(n):
    for j in range(0,i+1):
        print("#",end=" ")
    print()"""
"""from array import*
v=array('u',['e','h','h'])
print(v)
print(v.buffer_info())
v.reverse()
print(v)"""

'''import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))'''

#0-D
"""import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)"""

#2-D
"""import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)"""

"""import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)"""
"""import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)"""
'''import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])'''

import numpy as np

#
arr = np.array([1, 2, 3, 4, 5, 6, 7])

#print(arr[1:5:2])
#print(arr[::2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])








    

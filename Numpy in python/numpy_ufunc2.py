#NUMPY SUMMATIONS
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.sum([arr1,arr2])
print(arr3)
#Summation over an axis
newarr=np.sum([arr1,arr2],axis=0)
print(newarr)
#Cummulative sum means partially adding the elements in array.

#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

#Perfom partial sum with the cumsum() function
arr=np.array([1,2,3])
newarr=np.cumsum(arr)
print(newarr)

#NUMPY PRODUCTS
arr=np.array([1,2,3,4])
x=np.prod(arr)
print(x)
#REST EXPLORE AFTERWARDS AND THE TOPICS INCLUDES DIFFERENCES,FINDING LCM'S,GCD'S,TRIGONOMETRIC OPERATIONS,HYPERBOLIC OPERATIONS,SET OPERATIONS
#Without ufunc , we can use python's built in zip() method
# x=[1,2,3,4]
# y=[5,6,7,8]
# z=[]
# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)

# #NumPy has a ufunc for this, called add(x, y) that will produce the same result.
# import numpy as np
# x=[1,2,3,4]
# y=[5,6,7,8]
# z=np.add(x,y)
# print(z)

#Creating our own ufunc

#To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
#
#The frompyfunc() method takes the following arguments:
#
#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.
import numpy as np

# def myadd(x, y):
#     return x+y

# myadd = np.frompyfunc(myadd, 2, 1)

# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
# print(type(np.add))

arr1=np.array([11,12,13,14,15])
arr2=np.array([21,22,23,24,25])
newarr=np.add(arr1,arr2)
print(newarr)
newarr=np.subtract(arr1,arr2)
print(newarr)
newarr=np.multiply(arr1,arr2)
print(newarr)
newarr=np.divide(arr1,arr2)
print(newarr)
newarr=np.power(arr1,arr2)
print(newarr)
newarr = np.mod(arr1, arr2) #mod() and the remainder() functions return the remainder of the values
print(newarr)
newarr = np.remainder(arr1, arr2)
print(newarr)
newarr = np.divmod(arr1, arr2)#divmod() returns both quotient and mod
print(newarr)
arr=np.array([-1,-2,-3,-4,-5])
newarr=np.absolute(arr)
print(newarr)

#ROUNDING DECIMALS
#Five ways of rounding decimals in numpy
arr=np.trunc([-3.166,3.667]) #Truncation-Remove the decimals, and return the float number closest to zero.
print(arr)
arr=np.fix([-3.166,3.667])
print(arr)#fix() and trunc() methods are same
arr=np.around(3.1666,2)
print(arr)#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr=np.floor([-3.166,3.667])
print(arr)#The floor() function rounds off decimal to nearest lower integer
arr=np.ceil([-3.166,3.667])
print(arr)#The ceil() function rounds off decimal to nearest upper integer.

#NUMPY LOGS
arr=np.arange(1,10)
print(np.log2(arr))#Use the log2() function to perform log at the base 2.
print(np.log10(arr))
print(np.log(arr))#Use the log() function to perform log at the base e.
#Log at any base - NumPy does not provide any function to take log at any base,
#so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:
from math import log
nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))
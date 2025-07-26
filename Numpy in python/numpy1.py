import numpy as np

arr=np.array([1,2,3,4]) #1-d array

arr1=np.array(42) #0-d array

arr2=np.array([[1,2,3],[4,5,6]]) #2-d array

arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3-d array

print(arr.ndim) #.ndim command checks for dimensions
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#Higher dimension arrays
arr=np.array([1,2,3,4],ndmin=5) #This ndmin argument creates an array of the specified dimension which is 5 in this case
print(arr)
print("No of dimensions:",arr.ndim)

#Array indexing
arr=np.array([1,2,3,4])
print(arr[0]) #this is basically array indexing

arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element in the first row is: ',arr1[0,1]) #indexing in a 2D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #indexing in a 3D array
print(arr[0,1,2])

print('last element from 2nd dim: ',arr1[1,-1]) #negative indexing

#Array slicing
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
#Negative slicing is also same as in lists
#Slicing 2D arrays
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,1:4])
print(arr[::2]) #To print every other element from the entire array
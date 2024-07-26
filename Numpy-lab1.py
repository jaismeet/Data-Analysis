# convert the below list into numpy array than display the array 
# input : my_list=[1,2,3,4,5]

import numpy as np
my_list = [1,2,3,4,5]
arr = np.array(my_list)
print("Numpy array : \n" ,arr)

print("-----------------------------------------------------------------------------")

# convert the below list into a numpy array then display the array then display the  
# First and last index and then multiply each element by 2 and display the result
# input : my_list = [1,2,3,4,5]

my_list = [1,2,3,4,5]
arr = np.array(my_list)
print("First element : " , arr[0])
print("Second element : " , arr[-1])

print("Array after doubling each element : \n" , arr*2)

print("------------------------------------------------------------------------------")

# Write a Numpy program to create an array of 10 zeroes , 10 ones , and 10 fives.

arr1 = np.zeros(10 , int)
print("An array of 10 zeros : \n " , arr1)

arr2 = np.ones(10 , int)
print("An array of 10 ones : \n " , arr2)

arr3 = np.zeros(10,int) + 5
print("An array of 10 fives : \n " , arr3)

print("------------------------------------------------------------------------------")

# Write a Numpy program to create a 3*3 matrix with values ranging from 2 10 10 

arr4 = np.arange(2,11)
print(arr4)
matrix = arr4.reshape(3,3)
print("The 3*3 matrix is : \n" , matrix)

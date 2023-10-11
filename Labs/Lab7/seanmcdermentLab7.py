
import numpy as np
from scipy import stats
# NumPy allows for the Creation of Arrays
print('\n')
print("NumPy allows for the Creation of Arrays")
arr1 = np.array([12, 24, 32, 41, 5])
print("Array 1:", arr1)

arr2 = np.array([54, 42, 35, 35, 1])
print("Array 2:", arr2)

# NumPy allows you to perform mathmatical and  operations on arrays and Matrices
# The Scipy pluggin helps with statistical analysis of arrays
print('\n')
print("NumPy allows you to perform mathmatical operations on arrays")
sum_result = arr1 + arr2
print("Sum of arrays:", sum_result)
print('\n')
print("The NumPy pluggin is helped by the Scipy pluggin to help with statistical analysis of arrays")
averageOfArray1 = np.mean(arr1)
modeOfArray2 = stats.mode(arr2)
print("Average of Array 1:", averageOfArray1)
print("Mode of Array 2:", modeOfArray2)

# NumPy allows for the Creation of Matrices
print('\n')
print("NumPy allows for the Creation of Matrices")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


Multiresult = np.dot(matrix1, matrix2)
print("matrix 1:", matrix1)
print("matrix 2:", matrix2)
print('\n')
print("NumPy allows for the manipulation of Matrices")
print("Muliplication of matrices:", Multiresult)


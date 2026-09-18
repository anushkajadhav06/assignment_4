import numpy as np

matrix_a = np.array([[1, 2, 3], 
                     [4, 5, 6],
                     [5,4,3]])
print("matrix A")
print(matrix_a)

matrix_b = np.array([[7, 8, 9], 
                     [1, 2, 3],
                     [3,4,2]])
print("matrix B")
print(matrix_b)


result = matrix_a + matrix_b

print("Result:")
print(result)

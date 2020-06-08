'''
Accept data in two 3*3  matrix and calculate the sum of the matrices.
'''
import numpy as np
r = int(input("enter the rows you want:"))
c = int(input("enter the columns you want:"))
matrix1 = np.ndarray(shape=(r,c),dtype=int)
matrix2 = np.ndarray(shape=(r,c),dtype=int)

print(matrix1)
print(matrix2)

for i in range(r):
    for j in range(c):
        matrix1[i][j]=int(input("Enter matrix1 elements:"))
        matrix2[i][j]=int(input("Enter matrix2 elements:"))

print("----Matrix1-----")
print(matrix1)
print("-----Matrix2-------")
print(matrix2)
print("-----Sum of the two matrix-----")
print(matrix1+matrix2)
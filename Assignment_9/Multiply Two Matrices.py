# Solution 1
# Program to multiply two matrices

def initializeMatrix(n, v=0):
    M = []
    for i in range(n):
        # stor row
        row = []
        for j in range(n):
            row.append(v)
        M.append(row)
    return (M)


def createMatrix(n):
    M = []
    print("Enter the element :")
    for i in range(n):
        # stor row
        row = []
        for j in range(n):
            row.append(int(input()))
        M.append(row)
    return (M)


def printMatrix(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=" ")
        print()


def mulMatrix(A, B, result):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]
    return result


n = int(input("Enter N for N x N matrix: "))
M1 = createMatrix(n)

# Display the 2D array
print("Display Array M1 In Matrix Form")
printMatrix(M1, n)

M2 = createMatrix(n)

# Display the 2D array
print("Display Array M2 In Matrix Form")
printMatrix(M2, n)

sumMat = initializeMatrix(n)

for i in range(len(M1)):
    for j in range(len(M1[0])):
        sumMat[i][j] = M1[i][j] + M2[i][j]

print("Result Matrix")
for r in sumMat:
    print(r)


print("------------------------------RESTART------------------------------")


# Solution 2

# import numpy as np
#
# mat1 = np.array([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]])
#
# mat2 = np.array([[2, 3, 4],
#                  [5, 6, 7],
#                  [8, 9, 1]])
#
# sumMat = np.dot(mat1,mat2)
# print("The Product of two matrix \n\n{} and \n\n{} is \n\n{}".format(mat1,mat2,sumMat))
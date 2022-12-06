def intializeMatrix(n, v=0):
    M = []
    for i in range(n):
    # Store row
        row = []
        for j in range(n):
            row.append(v)
        M.append(row)
    return (M)

def createMatrix(n):
    M = []
    print("Enter the element : ")
    for i in range(n):
        # store row
        row = []
        for j in range(n):
            row.append(int(input()))
        M.append(row)

    return (M)

def printMatrix(M,n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end=" ")
        print()

def mulMatrix(A,B,result):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] = result[i][j] + A[i][k] *B[k][j]

    return result

n = int(input("Enter N for N x N matrix : "))
M1 = createMatrix(n)

# Display the 2D array
print("Display Array M1 in Matrix form")
printMatrix(M1, n)

M2 = createMatrix(n)

# Display the 2D Array
print("Display array M2 in Matrix form")
printMatrix(M2, n)

result = intializeMatrix(n)

result = mulMatrix(M1, M2, result)
print("Result Matrix")
for r in result:
    print(r)


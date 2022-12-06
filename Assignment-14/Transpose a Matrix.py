def initializeMatrix(n, v=0):
    M = []
    for i in range(n):
        # store row
        row = []
        for j in range(n):
            row.append(v)
        M.append(row)
    return (M)

def creatMatrix(n):
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
            print(M[i][j],end=" ")
        print()

def transposeMatrix(M,n,result):
    for i in range(n):
        for j in range(n):
            result[i][j] = M[j][i]
    return result

n = int(input("Enter N for N x N matrix : "))
M1 = creatMatrix(n)

# Display the 2D array
print("Display Array M1 in Matrix form")
printMatrix(M1, n)

result = initializeMatrix(n)
result = transposeMatrix(M1, n, result)
print("Transposed Matrix")
for r in result:
    print(r)


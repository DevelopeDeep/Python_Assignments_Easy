# solution 1

def main():
    mat1 = [[1, 6, 4],
            [4, 5, 6],
            [7, 6, 9]]

    mat2 = [[2, 5, 4],
            [5, 8, 7],
            [8, 3, 1]]

    sumMat = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    sumMat = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    print("The Sum of two matrix {} and {} is \n{} ".format(mat1,mat2,sumMat))

if __name__=="__main__":
    main()

print("------------------------RESTART------------------------")


# solution 2
# def main():
#
#     import numpy as np
#
#     mat1 = np.array([[1, 6, 4],
#                      [4, 5, 6],
#                      [7, 6, 9]])
#     mat2 = np.array([[2, 5, 4],
#                      [5, 8, 7],
#                      [8, 3, 1]])
#
#     sumMat = np.add(mat1, mat2)
#     print("The Sum of two matrix \n\n{}  and \n\n{}  is \n\n{} ".format(mat1, mat2, sumMat))
#
# if __name__=="__main__":
#     main()
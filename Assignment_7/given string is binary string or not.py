def CheckBinary(str):

    binary = "01"
    for i in range(len(str)):
        if str[i] not in binary:
            print("Not Binary")
            break
    else:
        print("Its a Binary")

str = input("Enter the string : ")
CheckBinary(str)

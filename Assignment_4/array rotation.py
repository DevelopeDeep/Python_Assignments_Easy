def main():
    lst = []
    n = int(input("Enter the length of your list : "))

    for i in range(n):
        lst.append(int(input()))
    print("The list is", lst)
    rotation = input("Enter Rotation right/left : ")
    nele = int(input("Enter the number of element to rotate < : "))
    if nele > n:
        print("can not rotate as element to rotate is larger then list length")
    else:
        rlst = []
        if rotation.upper() == "RIGHT":
            rlst[:] = lst[-nele:] + lst[:(n-nele)]
            print("After right rotation : ", rlst)
        elif rotation.upper() == "LEFT":
            rlst[:] = lst[nele:n] + lst[:nele]
            print("After left rotation : ", rlst)
        else:
            print("Invalid Entry")

if __name__=="__main__":
    main()
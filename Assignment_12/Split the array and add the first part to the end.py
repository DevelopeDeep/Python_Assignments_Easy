def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The list is ", lst)

    nele = int(input("Enter the number of element to split < : "))
    if nele > n:
        print("can not split as element to split is larger then list length")
    else:
        print("The split list is : ", lst[:nele])
        lst[:] = lst[nele:n] + lst[: nele]
    print("The list after split and add : ", lst)

if __name__=="__main__":
    main()

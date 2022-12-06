def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The List is : ", lst)
    lst.sort()
    print("The sorted list is : ", lst)
    nlargest = int(input("Enter how many largest number you want to see in from the list : "))

    if n < nlargest:
        print("Enter value is larger then that list length")
    else:
        print(nlargest, "largest element from the list are : ", lst[(n-nlargest):])

if __name__=="__main__":
    main()

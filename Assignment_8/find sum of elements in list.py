def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))

    print("The list is : ", lst)
    print("Sum of element in list : ", sum(lst))

if __name__=="__main__":
    main()
    
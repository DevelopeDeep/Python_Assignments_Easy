def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The List is ", lst)

    evenlist = []

    for i in lst:
        if i % 2 == 0:
            evenlist.append(i)
    print("The even number in the list is : ", evenlist)

if __name__=="__main__":
    main()
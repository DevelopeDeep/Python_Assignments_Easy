def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The list is : ", lst)

    oddlist = []

    for i in lst:
        if i % 2 != 0:
            oddlist.append(i)
    print("The odd number in list is : ", oddlist)

if __name__=="__main__":
    main()

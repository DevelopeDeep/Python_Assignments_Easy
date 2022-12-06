def main():

    n = int(input("Enter the length of your list : "))
    lst = []
    for i in range(n):
        lst.append(int(input()))
    print("The list is : ", lst)
    ele = int(input("Enter the element to find its occurrence : "))
    print(ele, "Has occurred {} times in the list : ".format(lst.count(ele)))


if __name__ == "__main__":
    main()

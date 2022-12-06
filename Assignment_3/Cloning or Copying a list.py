def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The list is : ", lst)

    print("The cloned/copied list is bellow : ")

    # Method 1
    lystcopy = lst[:]
    print("Cloning By list slicing lst [:] : ", lystcopy)

    # Method 2
    lst2 = lst.copy()
    print("Cloning By list copying lst.copy : ", lst2)

    # Method 3
    lstcompreh = [i for i in lst]
    print("Cloning By list Comprehension : ", lstcompreh)

    # Method 4
    lstappend = []
    for i in lst : lstappend.append(i)
    print("Cloning By list append : ", lstappend)

if __name__=="__main__":
    main()

# solution 1
def main():

    lst = [100, 240, 310, 67, 445, 9]
    max(lst)
    print(lst)
    print("largest element in the array is : {}".format(max(lst)))

if __name__=="__main__":
    main()


print("-------------------------RESTART------------------------------")


# Solution2
def main():

    lst = [100, 240, 310, 67, 445, 9]
    big = 0
    for i in range(0, len(lst)):
        if big < lst[i]:
            big = lst[i]
    print(lst)
    print("Largest element in the array is : {} ".format(big))

if __name__=="__main__":
    main()
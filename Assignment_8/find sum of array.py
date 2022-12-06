# Solution 1

def main():

    lst = [1,2,3,4,5,6,7,8,9]
    print(sum(lst))

if __name__=="__main__":
    main()

print("---------------------------RESTART--------------------------------")


# Solution 2
def main():
    sum = 0
    lst = [1,2,3,4,5,6,7,8,9]
    for i in range(0,len(lst)):
        sum += lst[i]
    print("Sum is : ", sum)

if __name__=="__main__":
    main()
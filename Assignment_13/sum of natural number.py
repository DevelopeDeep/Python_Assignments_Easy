def main():
    num = int(input("Enter the number : "))
    sum = 0
    for i in range(0, num + 1):
        sum += i
    print("Sum of natural number uotp {} is : {}".format(num, sum))


if __name__=="__main__":
    main()
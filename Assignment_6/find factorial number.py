def main():
    num = int(input("Enter a Number to find factorial : "))
    factorial = 1

    if num < 0:
        print("Can not calculate Factorial of a negative Number")
    elif num == 0:
        print("Factorial zero is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i

    print("Factorial of {} is : {}".format(num, factorial))

if __name__=="__main__":
    main()
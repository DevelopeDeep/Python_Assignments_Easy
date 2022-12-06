# Factorial of a number

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

def main():
    num = int(input("Enter a number to find factorial : "))
    if num < 0:
        print("cn not calculate factorial of a negative number")
    elif num == 0:
        print("factorial of zero is 1")
    else:
        print("factorial of {} is : {}".format(num, fact(num)))

if __name__=="__main__":
    main()
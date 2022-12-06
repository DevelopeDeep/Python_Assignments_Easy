
def main():

    num1 = int(input("Enter a number : "))

    if num1 > 1:
        for i in range(2, num1):
            if (num1 % i) == 0:
                print(num1, 'is not a prime')
                break
        else:
            print(num1, 'is a prime number')
    else:
        print("Number is less than 1")

if __name__=="__main__":
    main()
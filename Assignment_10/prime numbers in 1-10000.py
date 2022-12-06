def main():
    listprime = []

    num1 = int(input("Enter a number1 : "))
    num2 = int(input("Enter a number2 : "))
    for num in range(num1, num2):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, 'is not a prime number')
                    break
            else:
                print(num, 'is a prime number')
                listprime.append(num)


if __name__=="__main__":
    main()

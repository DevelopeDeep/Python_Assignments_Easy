def main():
    num1 = int(input("Enter any first Number : "))
    num2 = int(input("Enter any second Number : "))

    for i in range(1, int(num1/2)):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    print(gcd)
    
if __name__=="__main__":
    main()

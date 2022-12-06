def main():
    num = int(input("Enter a Number to display its multiplication table : "))
    print("\nmultiplication table for number {} is\n".format(num))

    for i in range(1, 11):
        print("{} x {}  = {}".format(num, i, i*num))

if __name__=="__main__":
    main()
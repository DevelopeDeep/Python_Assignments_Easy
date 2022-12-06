print("Demonstrate the testing K^K==N?")

def testing(n, k):
    formula = n == k ** k
    return formula

def main():
    print("enter value: ")
    num1 = int(input())
    print("enter value: ")
    num2 = int(input())

    total = testing(num1,num2)
    print("ans is :",total)

if __name__=="__main__":
    main()
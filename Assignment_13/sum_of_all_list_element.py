print("Demonstrate the sum of all list element")

def numbers(a, b, c):
    formula = (a+b+c)
    return formula

def main():
    print("enter first value: ")
    num1 = int(input())
    print("enter second value")
    num2 = int(input())
    print("enter third value: ")
    num3 = int(input())

    total = numbers(num1,num2,num3)
    print("list",[num1,num2,num3])
    print("Total Of list is: ",total)

if __name__=="__main__":
    main()
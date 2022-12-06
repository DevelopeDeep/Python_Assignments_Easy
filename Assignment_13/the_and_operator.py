print("Demonstrate the and Operator")

def numbers(a, b):
    formula = a and b
    return formula

def main():
    print("enter the value1: ")
    num1 = str(input())
    print("enter the value2: ")
    num2 = str(input())

    total = numbers(num1, num2)
    print("your answer is: ",total)

if __name__=="__main__":
    main()
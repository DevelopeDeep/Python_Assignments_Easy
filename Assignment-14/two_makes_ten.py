# two makes ten
def Makes(a, b):
    formula = bool(a+b ==10 or a ==10 or b ==10)
    return formula
def main():
    print("enter value1: ")
    num1 = int(input())
    print("enter value2: ")
    num2 = int(input())

    sum = Makes(num1,num2)
    print("the value is: ",sum)

if __name__=="__main__":
    main()
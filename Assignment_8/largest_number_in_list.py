print("Demonstrate the largest number in list")

def numbers(value1, value2, value3, value4):
    formula = max(value1, value2, value3, value4)
    return formula

def main():
    print("any first value")
    num1 = input()
    print("any second value")
    num2 = input()
    print("any third value")
    num3 = input()
    print("any forth value")
    num4 = input()

    large = numbers(num1, num2,num3,num4)
    print("List",[num1,num2,num3,num4])
    print("largest number is",large)

if __name__=="__main__":
    main()
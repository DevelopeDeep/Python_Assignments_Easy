print("Demonstrate the return last element in list")

def last(value1, value2, value3):
    formula = (value1, value2, value3)
    return formula
def main():
    print("Enter First value: ")
    num1 = input()
    print("Enter second value: ")
    num2 = input()
    print("Enter third value: ")
    num3 = input()

    sum = last(num1, num2, num3)
    print("list",[num1, num2, num3])
    print("the last element is: ",sum[-1])

if __name__=="__main__":
    main()
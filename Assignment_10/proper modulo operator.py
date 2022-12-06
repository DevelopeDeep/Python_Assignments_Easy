# Demonstrate the proper modulo operator

def modulo(value1, value2):
    formula = value1 % value2
    return formula

def main():
    print("Enter the value1: ")
    num1 = int(input())
    print("Enter the value2; ")
    num2 = int(input())

    total = modulo(num1,num2)
    print("The ans is: ",total)

if __name__=="__main__":
    main()

# Demonstrate are the numbers equal?

def numbers(value1, value2):
    formula = value1 == value2
    return formula

def main():
    print("Enter Value1: ")
    num1 = (input())

    print("Enter value2: ")
    num2 = input()

    total = numbers(num1,num2)
    print("Ans is: ",total)

if __name__=="__main__":
    main()
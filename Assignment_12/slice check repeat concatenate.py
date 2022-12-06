# Demonstrate the slice check repeat concatenate

def numbers(value1):
    formula = (value1[0:3]*3)
    return formula

def main():
    print("Enter Value1: ")
    num1 = input()

    total = numbers(num1)
    print("Ans is: ",total)

if __name__=="__main__":
    main()
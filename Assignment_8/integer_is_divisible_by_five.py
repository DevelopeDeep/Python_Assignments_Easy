print("Demonstrate the integer is divisible by five")

def value(a):
    formula = bool(a%5==0)
    return formula

def main():
    print("Enter value: ")
    num1 = int(input())
    total = value(num1)
    print("Divisible by five is: ",total)

if __name__=="__main__":
    main()
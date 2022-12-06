print("Demonstration of compare str by count of characters")

def numbers(a, b):
    formula = len(a)==len(b)
    return formula
def main():
    print(" Enter value1: ")
    num1 = str(input())
    print("Enter value2: ")
    num2 = str(input())

    total = numbers(num1, num2)
    print("Count of Characters is: ",total)

if __name__=="__main__":
    main()

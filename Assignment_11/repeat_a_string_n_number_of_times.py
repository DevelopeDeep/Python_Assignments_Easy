print("Demonstrate recursion repeat a string n number of times")

def numbers(a,b):
    formula = a*b
    return formula

def main():
    print("enter the value: ")
    num1 = str(input())
    print("enter value: ")
    num2 = int(input())

    total = numbers(num1,num2)
    print("Ans is: ",total)

if __name__=="__main__":
     main()

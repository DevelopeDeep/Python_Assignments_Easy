# Calculator with 4 basic mathematical operations
def main():
    num1 = float(input("Enter num1 : "))
    operation= input("Use operation : ")
    num2 = float(input("Enter num2 : "))

# "Enter + for addition : \nEnter - for subtraction :\nEnter * for multiplication :\nEnter / for division : "

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    if operation == "+":
        print("{} + {} = {}".format(num1,num2,add))
    elif operation == "-":
        print("{} - {} = {}".format(num1,num2,sub))
    elif operation == "*":
        print("{} * {} = {}".format(num1, num2, mul))
    elif operation == "/":
        if num1 == 0 or num2 == 0:
            print("division with zero is not possible")
        else:
            div = num1 / num2
            print("{} / {} = {}".format(num1, num2, div))
    else:
        print("Invalid input")

if __name__=="__main__":
    main()
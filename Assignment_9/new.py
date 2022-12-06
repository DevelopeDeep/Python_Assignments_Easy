# Demonstrate the repeat string

def repeat_string(text, n):

    if type(text) == str:
        return text * n
    else:
        return "Not A String !!"

def main():

    print("Enter value1")
    num = input()
    print("Enter value2")
    num1 = int(input())

    total = repeat_string(num,num1)
    print("Ans is:",total)

if __name__=="__main__":
    main()
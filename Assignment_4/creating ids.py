# Demonstrate the school ids

def equation(value1, value2):
    formula = (value1[:1].lower()+value2[0:1].upper()+value2[1:3].lower())
    return formula

def main():
    print("First Name:")
    num1 = input()
    print("Last Name")
    num2 = input()

    total = equation(num1,num2)
    print("Your ID is:",total)

if __name__=="__main__":
    main()
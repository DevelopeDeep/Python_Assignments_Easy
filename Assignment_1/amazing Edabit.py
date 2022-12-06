# Demonstrate the Amazing Edabit

def equation(value):
    formula = value
    if 'edabit' in value:
        print(value)
    elif value == value:
        print(value.replace("amazing", "not amazing"))
    return formula

def main():
    print("Enter value")
    num = input()

    total = equation(num)

if __name__=="__main__":
    main()

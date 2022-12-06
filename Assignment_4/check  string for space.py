# Demonstrate the check string for space

def equation(value):
    formula = " " in value
    return formula

def main():
    print("Enter Text:")
    num = input()

    total = equation(num)

    print("Is_the_space in between:",total)

if __name__=="__main__":
    main()
# Demonstrate the broken bridge

def equation(value):
    formula = ' ' not in value
    return formula

def main():
    print('enter value:')
    num = input()

    total = equation(num)
    print("ans is:",total)

if __name__=="__main__":
    main()




# Demonstrate the word singular or plural

def word(value):
    formula = value.endswith('s')
    return formula
def main():
    print("enter your text")
    num = input()

    total = word(num)
    print("ans is:",total)

if __name__=="__main__":
    main()
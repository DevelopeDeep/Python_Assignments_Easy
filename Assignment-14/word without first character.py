# Demonstration of word without first chracter

def word(text):
    formula = text[1:]
    return formula

def main():
    print("Enter the value:")
    num1 = input()

    total = word(num1)
    print("Ans is:",total)

if __name__=="__main__":
    main()
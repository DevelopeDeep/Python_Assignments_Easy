# Demonstrete the wordcharword

def word(char,text):
    # formula = char.join(text.split())
    formula = text.replace(' ', char)
    return formula

def main():
    print("Enter the value:")
    num1 = input()
    print("Enter the value:")
    num2 = input()

    total = word(num1, num2)
    print("Ans is:",total)

if __name__=="__main__":
    main()
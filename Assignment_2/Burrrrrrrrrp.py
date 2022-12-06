# Demonstrate the Burrrrrrp and Edaaaaabit use a many times

# def burp(value):
#     # formula = 'Bu' + 'r' * value + 'p'
#     return formula
#
# def main():
#     print("Enter text:")
#     num = int(input())
#
#     total = burp(num)
#     print("Ans is:",total)
#
# if __name__=="__main__":
#     main()

# next example

def eq(value):
    formula = "Ed{}bit".format("a" * value)
    return formula

def main():
    print("Enter the number:")
    num1 = int(input())

    total = eq(num1)
    print("ans is :", total)

if __name__ == "__main__":
     main()
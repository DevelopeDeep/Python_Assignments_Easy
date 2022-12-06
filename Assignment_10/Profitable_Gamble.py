print("Demonstrate the profitable Gamble")

def profit(prob, price, pay):
    formula = bool(prob*price>pay)
    return formula
def main():
    print("Enter prob value: ")
    num1 = float(input())
    print("Enter price: ")
    num2 = float(input())
    print("Enter pay amount: ")
    num3 = float(input())

    total = profit(num1, num2, num3)
    print("Profitable Gamble is: ",total)

if __name__=="__main__":
    main()


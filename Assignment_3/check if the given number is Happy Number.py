# A number is said to be happy if it yields 1
# when replaced by the sum of squares of its digits
# repeatedly. If this process results in an
# endless cycle of numbers containing 4, then the
# number will be an unhappy number.

def isHappy(num):
    sum = 0
    while(num>0):
        digit = num % 10
        sum = sum + digit ** 2
        num = num//10
    return sum

def main():

    num = int(input("Enter the number : "))
    result = num

    while (result != 1 and result != 4):
        result = isHappy(result)

    if result == 1:
        print(num, "Is a Happy Number")
    else:
        print(num, "Is a Unhappy Number")

if __name__=="__main__":
    main()

# If a number is divisible by the sum of its digits,
# then it will be known as a Harshad Number

def digitSum(num):
    sum = 0
    while(num>0):
        digit = num % 10
        sum = sum + digit
        num = num // 10
    return sum

def main():
    num = int(input("Enter the number : "))
    sum = digitSum(num)

    if num % sum == 0:
        print(num, "Is a Harshad Number")
    else:
        print(num, " Is not a Harshad number")

if __name__=="__main__":
    main()
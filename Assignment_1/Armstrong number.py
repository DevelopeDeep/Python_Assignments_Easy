# Demonstrate the Armstrong number
# 153 = length = 3
# 1*1*1 = 1
# 5*5*5 = 125
# 3*3*3 = 27
# sum = 1 + 125 + 27 = 153
# num = sum
def main():
    num = int(input("Enter the Number : "))
    power = len(str(num))

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** power
        temp = temp // 10
    if num == sum:
        print("Number is Armstrong Number")
    else:
        print("Not an Armstrong Number")

if __name__=="__main__":
    main()
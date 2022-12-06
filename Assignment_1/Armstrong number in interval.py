def main():
    # fining for a range of numbers
    low = int(input("Lower Limit : "))
    up = int(input("Upper Limit : "))

    for num in range(low,up+1):
        power = len(str(num))
        temp = num
        sum = 0

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** power
            temp = temp// 10
            if num == sum:
                print(num)

if __name__=="__main__":
    main()
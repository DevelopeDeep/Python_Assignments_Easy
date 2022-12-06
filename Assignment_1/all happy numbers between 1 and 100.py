def isHappy(num):
    sum = 0
    while(num>0):
        digit = num%10
        sum= sum + digit**2
        num = num//10
    return sum

def main():

    print("Happy numbers in range 1 to 100")
    result = num = i = 0
    happyNum = []
    for i in range(1, 101):
        result = i
        while (result != 1 and result != 4):
            result = isHappy(result)
        if result == 1:
            happyNum.append(i)
    print(happyNum)

if __name__=="__main__":
    main()
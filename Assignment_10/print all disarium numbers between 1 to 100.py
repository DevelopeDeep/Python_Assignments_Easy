def isDisarium(num):

    sum = 0
    while(num>0):
        dgcnt= len(str(num))
        digit = num % 10
        sum = sum + digit**dgcnt
        dgcnt -= 1
        num = num//10
    return sum

def main():
    print("Disarium numbers in range 1 to 100")
    disariumNum = []

    for i in range(1, 101):
        sum = isDisarium(i)
        if sum == i:
            disariumNum.append(i)
    print(disariumNum)

if __name__=="__main__":
    main()


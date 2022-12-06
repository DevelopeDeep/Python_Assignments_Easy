def isDisarium(num):
    sum = 0
    while(num>0):
        dgcnt= len(str(num))
        digit = num%10
        sum= sum + digit**dgcnt
        dgcnt-=1
        num = num//10
    return sum

num = int(input("Enter the number :"))


sum = isDisarium(num)
if sum == num:
    print(num,"Number is Disarium")
else:
    print(num,"Number is not Disarium")
# The pronic number is a product of two
# consecutive integers of the form: n(n+1).

def isPronicNum(num):
    isPronic = False
    for i in range(1, num + 1):
        if i * (i+1) == num:
            isPronic = True
    return isPronic

def main():
    print("Pronic number in range 1 to 100")
    pronicNum = []
    for i in range(1, 101):
        if isPronicNum(i):
            pronicNum.append(i)
    print(pronicNum)

if __name__=="__main__":
    main()
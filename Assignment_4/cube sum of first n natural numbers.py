def main():

    n = int(input("Enter n : "))
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    print("Cube sum of {} natural number is : {}".format(n, sum))

if __name__=="__main__":
    main()
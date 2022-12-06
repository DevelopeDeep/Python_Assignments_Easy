# Fibonacci series :- 1,1,2,3,5,8,13.........
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
def main():
    sequence = int(input("Enter a number to find the fibonacci series : "))

    if sequence <= 0:
        print("Please enter a positive number")
    elif sequence == 1:
        print("fibonacci series upto", sequence, ":")
    else:
        print("Fibonacci series upto ", sequence, ":")
        for i in range(sequence):
            print(fibo(i), end=' ')
    print()


if __name__=="__main__":
    main()
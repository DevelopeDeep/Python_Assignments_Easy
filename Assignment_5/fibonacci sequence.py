# Fibonacci series -> 1, 1, 2, 3, 5, 8, 13...........
def main():
    sequence = int(input("Enter the number to find fibonacci series : "))
    count = 0
    a, b = 0, 1

    if sequence <= 0:
        print("Please enter a positive number")
    elif sequence == 1:
        print("Fibonacci series upto", sequence, ":")
        print(a)
    else:
        print("Fibonacci series upto", sequence, ":")
        while count <= sequence:
            print(a, end=" ")
            c = a + b
            a, b = b, c
            count += 1

if __name__=="__main__":
    main()
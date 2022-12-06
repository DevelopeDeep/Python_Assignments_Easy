# An array is said to be monotonic in nature if it is either continuously increasing or continuously decreasing.
def main():

    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The List is ", lst)

    if all((lst[i] <= lst[i+1] for i in range(n-1)) or (lst[i] >= lst[i+1] for i in range(n-1))):
        print("Monotonic")
    else:
        print("Not Monotonic")

if __name__=="__main__":
    main()
def main():
    n = int(input("Enter the length of your list : "))
    lst = []

    for i in range(n):
        lst.append(int(input()))
    print("The List is : ", lst)
    Product = 1
    for ele in lst:
        Product = Product * ele
    print("Product of element in list is : ", Product)

if __name__=="__main__":
    main()

def main():
     n = int(input("Enter the length of your list : "))
     lst = []

     for i in range(n):
         lst.append(int(input()))
     print("The List is : ", lst)
     print("The Smallest element in list is : ", min(lst))

if __name__=="__main__":
    main()


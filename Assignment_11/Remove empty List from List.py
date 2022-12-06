def main():
    lst = [2, [], 4, 5, [], 6, 8, [], 3]

    print("The list : ", lst)
    removedlist = [ele for ele in lst if ele != []]
    print("The list after removing empty list")
    print(removedlist)

if __name__=="__main__":
    main()

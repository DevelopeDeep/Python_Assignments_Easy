def main():

    str = input("Enter the string a : ").lower()
    duplicate = []

    for i in str:
        if str.count(i) > 1:
            if i not in duplicate:
                duplicate.append(i)

    print(duplicate)

if __name__=="__main__":
    main()



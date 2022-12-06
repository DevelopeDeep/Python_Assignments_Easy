def main():
    str = input("Enter Names : ")

    words = str.split()
    words.sort()
    for word in words:
        print(word)

if __name__=="__main__":
    main()
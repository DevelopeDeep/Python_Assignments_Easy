def main():

    import string

    string_char = string.punctuation
    spChar = []

    str = input("Enter the string a : ").lower()
    for i in str:
        if i in string_char:
            spChar.append(i)
    if len(spChar) > 0:
        print("String {} in has special character/s is : {}".format(str, spChar))

if __name__=="__main__":
    main()
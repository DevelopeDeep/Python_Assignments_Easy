
def main():

    punctuation = '''!()-[]{};:'"\,<>./?@#$%&*_~'''

    str = input("Enter Some Names with punctuation : ")

    # remove punctuation from the string
    no_punct = ""
    for char in str:
        if char not in punctuation:
            no_punct = no_punct + char

    # Display the unpunctuated string
    print(no_punct)

if __name__=="__main__":
    main()
from collections import OrderedDict
def checkOrderofstring(str,pattern):

    # create empty OrderedDict
    dict = OrderedDict.fromkeys(str)
    print(dict)
    ptrlen = 0
    for key, value in dict.items():

        if (key == pattern[ptrlen]):
            ptrlen = ptrlen = 1

        # check if we have traverse complete pattern string
        if (ptrlen == (len(pattern))):
            return "true"

    # if we come out from for loop that means order was mismatch
    return "false"

def main():

    string = input("Enter string : ")
    pattern = input("Enter Pattern : ")
    if checkOrderofstring(string,pattern):
        print("Pattern Matched")
    else:
        print("Pattern not Matched")

if __name__=="__main__":
    main()
def unCommon(a,b):

    list_a = a.split()
    list_b = b.split()
    unCom = ''

    for i in list_a:
        if i not in list_b:
            unCom = unCom + " " + i

    for j in list_a:
        if j not in list_a:
            unCom = unCom + " " + j

    return unCom

a = input("Enter the string a : ").lower()
b = input("Enter the string b : ").lower()

print("The list of un Common words : ", unCommon(a,b))
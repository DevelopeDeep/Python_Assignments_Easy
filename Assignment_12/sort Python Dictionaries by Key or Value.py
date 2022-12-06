def main():

    a = {1: 2, 2: 1, 4: 3, 3: 4, 6: 5, 5: 6}

    # this will print a sorted list of the keys
    print(sorted(a.keys()))

    # this will print the sorted list with items.
    print(sorted(a.items()))

    a = {1: 2, 2: 1, 4: 3, 3: 4, 6: 5, 5: 6}

    print(sorted(a.values()))
    # this will print a sorted list of values.

if __name__=="__main__":
    main()
print("Demonstrate the name greeting!")

def greeting(value1):
    ans = ("Hello"+ ' '+ value1 + "!")
    return ans

def main():
    print("Hi Tom! ")
    name = input()

    sum = greeting(name)
    print(sum)

if __name__=="__main__":
    main()
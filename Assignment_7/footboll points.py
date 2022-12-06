# Demonstrate the football point

def Points(wins, draws, losses):
    formula = wins*3+draws*1+losses*0
    return formula

def main():
    print("Wins: ")
    num1 = int(input())

    print("draws: ")
    num2 = int(input())

    print("losses: ")
    num3 = int(input())

    total = Points(num1,num2,num3)
    print("Total Point of team is: ",total)

if __name__=="__main__":
    main()
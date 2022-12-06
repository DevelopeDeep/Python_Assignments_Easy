print("Demonstration Area of Triangle")
import logic_module

def main():
    print("Triangle Base: ")
    Base = float(input())
    print("Triangle Height is: ")
    Height = float(input())
    print("Divided by 2: ")
    div_Value = int(input())
    formula = logic_module.Triangle(Base, Height, div_Value)
    print("The area of Triangle is: ",formula)
if __name__=="__main__":
    main()
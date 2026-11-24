def acadper():
    stuname=input("Enter students name : ")
    eng=int(input("Enter english mark : "))
    maths=int(input("Enter maths mark : "))
    sci=int(input("Enter science mark : "))
    soc=int(input("Enter social mark : "))
    tam=int(input("Enter tamil mark : "))
    tot=eng+maths+sci+soc+tam
    per=tot/5
    if per<=100:
        print(stuname," is ready for 69")
        print("Total marks is ",tot)
        print("Percentage is ",per)
        if per>90:
            print("Grade is S")
        elif per>80:
            print("Grade is A")
        elif per>60:
            print("Grade is B")
        elif per>40:
            print("Grade is C")
        else :
            print("Better luck next time")
    else:
        print("Marks entered might be wrong")
acadper()

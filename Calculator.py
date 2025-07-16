#Calculator in Python .

#Functions 

def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    if b==0:
        return "Zero isnt Divisible"
    return(a/b)

#Program

while True:
    print("Welcome to My Calculator : ")
    print("Select Your Service No : ")
    print("Menu\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. All in One")

    choice=eval(input("Choose Your Services from MENU (1-5) : "))

    #Input Details

    a=float(input("Enter Number 1 / a :"))
    b=float(input("Enter Number 2 / b :"))

    if choice==1:
        print("Result = ",add(a,b))

    if choice==2:
        print("Result = ",subtract(a,b))

    if choice==3:
        print("Result = ",multiply(a,b))

    if choice==4:
        print("Result = ",division(a,b))

    if choice==5:
        print("\nAddition : ",add(a,b),
              "\n Subtract :",subtract(a,b),
              "\n Multiply : ",multiply(a,b),
              "\n Division",division(a,b),"\n")

    else:
        print("Sorry This Function Isnt Available : Select from (1-5)")

    again=input("Do You Want to Continue and Calculate again ? (Yes/No) :").lower()
    if again != "yes":
        print("Thank you for using my Calculator Project")
        break

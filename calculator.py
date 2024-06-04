print("Choose Operation.\n")

print("Add for Addition")
print("Sub for Subtraction")
print("Mul for Multiplication")
print("Div for Division")

Addition = "Add"
Subtraction = "Sub"
Multiplication = "Mul"
Division = "Div"

num1 = 0
num2 = 999 


while True:
    operation = str(input("Select an operation:" ))
    operation = str(operation)
    print("You have selected:", operation)
    
    print("Please input first number: ")
    num1 = int(input())
    num1 = int(num1)
    
    print("Please input second number: ")
    num2 = int(input())
    num2 = int(num2)
    
        if operation == "add":
            print(num1 + num2)
        
 
  
        

    
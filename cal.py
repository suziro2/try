num_1 = int(input("Enter num1 : ")) 
num_2 = int(input("Enter num2 : "))
operation = input("+,-,*,/")

if operation == "+":
    total = num_1+num_2
    print(total)

elif operation == "-":
    total = num_1-num_2
    print(total)

elif operation == "*":
    total = num_1*num_2
    print(total)

elif operation == "/":
    total = num_1/num_2
    print(total)

else:
    print("Error buang")


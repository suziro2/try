age = int(input("Enter your age : "))

if age > 65:
    print("senior citizen discount")

elif age >= 18 and age <= 64:
    print("regular ticket")

elif age < 18:
    print("child's ticket")
grade = int(input("enter a grade:"))

excellent = "90 above"
good =     "70 between 89"
Average =  "50 between 69"
fail =     "49 below"


if grade >= 90:
    print("excellent")

elif grade >= 70 and grade <=  89:
    print("good")

elif grade >= 50 and grade <=  69:
    print("Average")

elif grade >= 49:
    print("fail")

else:
    print("errors")


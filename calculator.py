def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def divide( x,y):
    if y == 0:
        return x / y
    
def cal():
    print("pls select option:")
    print("1. Add")
    print("2. SUb")
    print("3. Mul")
    print("4. Div")

    choice = input("Choices 1/2/3/4:")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input('Enter a fisrt num:'))
        num2 = float(input('Enter a second num:'))

        if choice == '1':
            print(f'result is: {add(num1,num2)}')
            
        elif choice == '2':
            print(f'result: {sub(num1,num2)}')

        elif choice == '3':
            print(f'result: {mul(num1,num2)}')

        elif choice =='4':
            print(f'result: {divide(num1,num2)}')

        else:
            print('Good shet')
cal()            



    


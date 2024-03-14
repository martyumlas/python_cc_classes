


is_valid = True
while is_valid:
    num1 = input('Enter number: ')
    num2 = input('Enter another number: ')
    try:        
        sum = int(num1) + int(num2) 
    except ValueError:        
        print('Enter Valid number')
    else:
        print(sum)
        break
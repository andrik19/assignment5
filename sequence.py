n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1,n+1):
    if i == 1:
        print('1')
        number1 = 1
    elif i == 2:
        print('2')
        number2 = 2
    elif i == 3:
        print('3')
        number3 = 3
    elif n > 3:
        number = number1 + number2 + number3
        print(number)
        number1 = number2
        number2 = number3
        number3 = number


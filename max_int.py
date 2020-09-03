max_int=0
num_int = int(input("Input a number: "))    # Do not change this line

while num_int > 0:
    max_int=max(num_int,max_int)
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line

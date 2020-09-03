max_int=0
num_int = int(input("Input a number: "))    # Do not change this line

while num_int > 0:
    max_int=max(num_int,max_int)
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line

#1) Ask the user for a number
#2) Find what number is  the largest with max()
#3) Ask the user for a number again
#   if the number is <= 0 go to #4
#   if the number is > 0 got back to #2
#4) End the loop and print the max number

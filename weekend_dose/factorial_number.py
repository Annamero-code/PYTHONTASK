#collect a number from user by casting 
#declear factoral and assign  1 to it
#use for loop to loop through it 
#multiply number by factorial i  declear ealier 
#print factorial as the final result




n = int(input("Enter a number: "))
factorial = 1

for number in range (1, n + 1):
    factorial *= number

print( factorial)


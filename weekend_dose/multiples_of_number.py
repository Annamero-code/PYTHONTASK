#declear a variable 'n' and assign an integer to it 
#declear a variable multiple and assign zero it 
#use for loop to loop throug the number and 
#use if statement that any number that is divisible by n from 1 to 100 without a remider is a multiple of n and 
#it should be store inside the variable multiple i declear ealier
#print statment to display the final answer
#





n = 6
multiples = 0
for number in range (1,101):
    if(number % n == 0):
        multiples += 1
print(multiples)
    

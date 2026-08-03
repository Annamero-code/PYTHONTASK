#declear even numbers to be zero
#declear odd numbers to be zero
#doing this because i dont know how many even & and odd number im going to have
#now out code list of numbers and assign them to a variable called number 
#use for loop to loop through the numbers
#now use the if statement and put a condition on it and use the mudulus operator (%)
#any number in the number list that is divisible by 2 without a reminder is even
#using the += that any even number you find on that number list store it into that variable we declear ealier
#use the elif statement ie any number that has a reminder divided by 2 should be store in the odd number variable 
#print statement to display the result for  even number and 
#print satement to display the result for the odd number
#
even_number = 0
odd_number = 0
number = [3,5,7,4,8,4,1,9]
for number in number:
    if number % 2 == 0:
        even_number += 1
    elif number % 2 != 0:
        odd_number += 1


print("even number here are just:", even_number)
print("odd number here are  just:", odd_number)
       

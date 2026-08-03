#Ask the user for a number.
#Convert it from text to an integer.
#Create a variable "answer"  starting at 0.
#Loop through every number from 1 to n.
#Add each number to answer.
#Print the final result.


n = int(input("Enter a number: "))
answer = 0

for number in range (1, n + 1):
    answer += number

print( answer)


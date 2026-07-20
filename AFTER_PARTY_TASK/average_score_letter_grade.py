
#psuedocode
//use int input to collect firt score from the user
//use int input to collect second  score from the user
//use int input to collect third score from the user
//use if statemnet to 
//to get the average sum all the firt score, second score and third score and use the floor divisor by 3
//and use elif statement to compare the condition
//use print to print the average score  and the letter grade

first_score = int(input("enter first score:"))

second_score = int(input("enter second score: "))

third_score = int(input("enter third score: "))

average = (first_score + second_score + third_score) // 3


if average >= 90 and average  <= 100:
	grade1 = "A"

elif average  >= 80 and average  <= 90:
	grade1 = "B"

elif average  >= 70 and average  <= 80:
	grade1 = "C"

elif average  >= 60 and average  <= 70:
	grade1 = "D"

else :
	grade1 = "F"

if average >= 90 and average  <= 100:
	grade2 = "A"

elif average  >= 80 and average  <= 90:
	grade2 = "B"

elif average  >= 70 and average  <= 80:
	grade2 = "C"

elif average  >= 60 and average  <= 70:
	grade2 = "D"

else :
	grade2 = "F"

if average >= 90 and average  <= 100:
	grade3 = "A"

elif average  >= 80 and average  <= 90:
	grade3 = "B"

elif average  >= 70 and average  <= 80:
	grade3 = "C"

elif average  >= 60 and average  <= 70:
	grade3 = "D"

else :
	grade3 = "F"


print("average: ", average )
print("letter grade: ", grade1)


print("letter grade: ", grade2)

print("letter grade: ", grade3)






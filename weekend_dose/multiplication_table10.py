#collect a number from user using by casting
#ask the user to enter any number from 1 to 10
#set number in range from 1 to 11
#print statement to display the result 
#use \t\ to give spaces for the table 
#



number = int(input("Enter from 1 to 10: "))
for table in range (1,11):
    print(number, 'x', table, '=', number*table, end = "\t")
   

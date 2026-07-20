#Exercises 2.9
#fine the sum, average and product from number you prompt user to input and also
#fine the the smallest and the lagest number out from the number 

sum = 0

average = 0

product = 0



number1 = int(input("Enter the first integer: "))

number2 = int(input("Enter the second integer: "))

number3 = int(input("Enter the third integer: "))

sum = number1 + number2 + number3

average = sum / 3

product = number1 * number2 * number3

smallest = number1

if number2 < smallest:
    smallest = number2

if number3 < smallest:
    smallest = number3



largest = number1

if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3


print("The sum value is", sum)

print("The average value is", average)

print("The product value is", product)

print("The smallest number value is", smallest)

print("The largest number value is", largest)





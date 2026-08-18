import random
def guess_game ():
    
        number = random.randint(1,1000)
print("Guess my number between 1 and 1000 with the fewest guesses:")
    
    
while True :
    guess = int(input("try your luck: "))
    
    if guess < 0 : break
    elif guess > number:
        print("Too high try again ")
    
    elif guess < number:
        print("Too low try again")
        
    else:
        print("congratulation you self no small")
        break

while True:
    guess_game()

    play_again = input("Would you like to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break      

  
  
  
  
  
  
  
  
  
  
  


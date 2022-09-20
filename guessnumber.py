n=18
guess=9
while(guess!=0):
    num =int(input("Enter the number you want to guess within 9 guesses\n"))
    if (num==18):
        print("You guess the correct number\n")
        guess=guess-1
        print("Game Over!! Guesses left:",guess)
        break
    elif num<18:
        print("Number entered is less than what you guessed, ENTER AGAIN!!\n")
        guess=guess-1
        print("Guesses left:",guess)    
    else:
        print("Number entered is greater than what you guessed, ENTER AGAIN!!\n")        
        guess=guess-1
        print("Guesses left:",guess)    
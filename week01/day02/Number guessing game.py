import random
class A():
    def r_game(self):
        r_num = random.randint(1,100)
        print("I picked a number between 1 and 100")
        attempt=7
        while True:
            guess = int(input("Enter your guess:  "))
            attempt -= 1
            diff = abs(guess - r_num)
            if attempt == 0:
                print("game over")
                print("the number was: ", r_num)
                break
            elif guess == r_num:
                print("your guess is correct")
                print("the number was: ", r_num)
                break
            elif guess>r_num:
                print("guess is high")
            elif guess<r_num:
                print("guess is low")
            else:
                print("invalid value")   
            print("attempts left: ",attempt)
a=A()
a.r_game()    
while True:
    playagain=input("Play again? y/n")
    if playagain=='y':
        a.r_game()
    else:
        print("game over")
        break


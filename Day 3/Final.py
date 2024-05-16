print("Welcome to Treasure Island")
print("Your mission is to find Treasure")

isGameOver = False

while not isGameOver:
    option1_left_right = input("Which way would you,like to go first, left or right?: ").lower()
    if option1_left_right == "left":
        option2_swim_wait = input("Would you like to go for a swim or wait for the boat (swim or wait)?: ").lower()
        if option2_swim_wait == "wait":
            option3_red_blue_yellow = input("Which do do you choose: red, blue, or yellow? ").lower()
            if option3_red_blue_yellow == "yellow":
                print("Treasure island!!!")
                isGameOver = True
                if isGameOver:
                    continue_or_not = input("Would you like to play again? (y/n) ")
                    if continue_or_not.lower() == "y":
                        isGameOver = False
                    else:
                        isGameOver = True
                        print("Thank you for playing!")
            else:
                print("You've lost")
                isGameOver = True
        else:
            print("You've lost")
            isGameOver = True
    else:
        print("You've lost")
        isGameOver = True

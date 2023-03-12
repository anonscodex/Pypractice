bash = 0
while bash != 3:
    bash = int(input("Enter your number: "))
    if (bash == 3):
        print("Game Over")
    elif (bash % 3 == 0):
        print("game over")
        break
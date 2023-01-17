
answer = input("Player 1: Please insert the number (1 - 100): ")
answer = int(answer)

is_correct = False
try_Count = 0

while try_Count < 10 and is_correct == False:
    guess = int(input("Player 2: please guess a Number! "))
    if guess == answer:
        print("player 2: You won!")
        is_correct = True
    elif guess > answer:
        print("Your guess is greater than the answer.")
        try_Count += 1
    else:
        print("Your guess is smaller than the answer.")
        try_Count += 1


if is_correct == False:
    print("player 2: You lost!")

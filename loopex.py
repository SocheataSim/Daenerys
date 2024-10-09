# import random

# secret_number = random.randint(0,100)
# guess = 0
# while guess != secret_number:
#     guess = int(input("Guess the secret number: "))
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
# print("Congratulations, you guessed it!")
import random
while True:
    secret_number = random.randint(1,100)
    print("Guess a magic number between 1 to 100: ")
    for attempt in range (1,6):
        guess = int(input(f"Attempts {attempt} enter your guessed number: " ))
        if guess == secret_number:
            print("Yes, you are correct! The number is ",secret_number)
        elif guess > secret_number:
            print("You are too high!")
        else:
            print("You are too low!")
    else:
        print("You have used all attempts", secret_number)

    play_again = input("Do you want to play again? (Yes/No):").lower()
    if play_again != 'Yes':
       print("Goodbye!")
       break

     
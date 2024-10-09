# import random
# #it is function
# #def guess_app():
# while True:
#     secret_number = random.randint(1,100)
#     print("Guess a magic number between 1 to 100: ")
#     for attempt in range (1,6):
#         guess = int(input(f"Attempts {attempt} enter your guessed number: " ))
#         if guess == secret_number:
#             print("Yes, you are correct! The number is ",secret_number)
#         elif guess > secret_number:
#             print("You are too high!")
#         else:
#             print("You are too low!")
#     else:
#         print("You have used all attempts", secret_number)

#     play_again = input("Do you want to play again? (Yes/No):").lower()
#     if play_again != 'Yes':
#        print("Goodbye!")
#        break


# #guess_app()
# for i in range(3):
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print(f"{number} is Even")
#     else:
#         print(f"{number} is Odd")

# def check_even_odd(number):
    
#     if number % 2 == 0:
#         print(f"{number} is Even")
#     else:
#         print(f"{number} is Odd")

# def main():
#     for i in range(3):
#         number = int(input("Enter a number: "))

#         check_even_odd(number)

# main()

# for i in range(3):
#     player_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     computer_choice = "rock"

#     if player_choice == computer_choice:
#        print("It's a tie!")
#     elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
#          print("You win!")
#     else:
#         print("You lose!")
# import random

# def determine_winner(player_choice, computer_choice):
    
#     if player_choice == computer_choice:
#         print("It's a tie!")
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "scissors" and computer_choice == "paper") or \
#          (player_choice == "paper" and computer_choice == "rock"):
#         print("You win!")
#     else:
#         print("You lose!")

# def main():
#     for _ in range(3):
#         player_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#         computer_choice = random.choice(["rock", "paper", "scissors"])
#         print(f"Computer chose: {computer_choice.capitalize()}")
#         determine_winner(player_choice, computer_choice)

# main()

# for i in range(3):
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You are an adult.")
#     else:
#         print("You are a minor.")
def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
def main():
    for _ in range(3):
        age = int(input("Enter your age: "))
        check_age(age)
        

main()
# def sunfunction():
#     sum =0 
#     for i in range(1,10):
#         sum+=i
#     return sum
# print(sunfunction())
   
    
  


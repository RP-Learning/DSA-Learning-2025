# Task 1: Even numbers from 1 to 20
print("Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# Task 2: Guess the number game
import random
secret = random.randint(1, 10)
guess = None
while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Correct! 🎉\n")

# Task 3: Sum from 1 to N
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum from 1 to {n} is: {total}")

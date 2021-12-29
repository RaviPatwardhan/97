import random
print("number guessing game")

number=random.randint(1,9)
chances=0
print("guess a number(bewteen 1 and 9)")
while chances<5:
    guess=int(input("enter your guess:   "))

    if guess==number:
        print("you won")
        break
    elif guess<number:
        print("your guess is to low, guess a higher number", guess)
    else: 
        print("your guess is to high, guess a lower number", guess)
    chances+=1

    if not chances<5:
        print("you lost, the number is",number)
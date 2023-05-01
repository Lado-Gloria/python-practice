
import random
secret_number = random.randint(1, 100)
tries = 0

while tries < 6:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number in", tries, "tries!")
        break
    elif guess < secret_number:
        print("Sorry, that's too low. Guess again.")
    else:
        print("Sorry, that's too high. Guess again.")


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Your random password is:", password)
import random

secret_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number in", tries, "tries!")
        break
    elif guess < secret_number:
        print("Sorry, that's too low. Guess again.")
    else:
        print("Sorry, that's too high. Guess again.")     
           
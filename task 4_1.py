#Choose a number between 1 and 10, and assign it to the variable "secret"
#Choose another number between 1 and 10, and assign it to the variable "guess"
#If guess is smaller than secret, print the string "too low"
#If guess is larger than secret, print the string "too high"
#If guess is equal to secret, print the string "just right"

secret=6
guess=7
if guess>6:
    print("too high")
elif guess==6:
    print("just right")
else:
    print("too low")

import secrets
import string
import random
import keyboard

while True:
    # Friendly welcome message :)
    print("")
    print("Hello! Thank you for using Nate's guaranteed super safe password generator!")
    print("Press spacebar to generate your new password!")

    # Wait for user to press space
    keyboard.wait("space")

    # Use a combination of letters A-Z + lowercase a-z, digits, and !$#
    puncChars = "!$&"
    characters = string.ascii_letters + string.digits + puncChars

    # Randomized length for the password that will be generated
    passLength = random.randrange(12, 18)

    # Generate password
    newPass = ''.join(secrets.choice(characters) for _ in range(passLength))

    # Print the user's new password :D
    print("")
    print('Your new password is:')
    print(newPass)
    print("")
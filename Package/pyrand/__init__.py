import string
import random

def passGenrator(characters_number):
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)


    while True:
        try:
            characters_number = int(characters_number)
            if characters_number < 6:
                return 'You Need At Least 6 characters'
            elif characters_number > 50:
                return "You Can't add more than 50 characters"
            else:
                break

        except:
            return 'Please Enter Numbers Only'

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))

    password = []

    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])

    for i in range(part2):
        password.append(s3[i])
        password.append(s4[i])

    password = "".join(password[0:])
    return password
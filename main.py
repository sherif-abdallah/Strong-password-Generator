import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("How Many characters for the password : ")

while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print('You Need At Least 6 characters')
            characters_number = input("Please Enter the number Again : ")
        elif characters_number > 50:
            print("You Can't add more than 50 characters")
            characters_number = input("Please Enter the number Again : ")
        else:
            break

    except:
        print('Please Enter Numbers Only')
        characters_number = input("How Many characters for the password : ")

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
print(password)
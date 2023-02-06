import random
import string

#function generating ten characters long password
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    password = ''.join(random.choice(letters + numbers + special_characters) for i in range(10))
    validate(password)

#function checking if password fulfills minimum criteria
def validate(password):
    t1 = 0
    t2 = 0
    t3 = 0
    for k in range(10):
        if password[k].isupper():
            t1 = 1
        elif password[k].isdigit():
            t2 = 1
        elif not password[k].isalnum():
            t3 = 1
        if t1 and t2 and t3:
            print(password)
            break
    if t1 == 0 or t2 == 0 or t3 == 0:
        generate_password()


if __name__ == '__main__':
    generate_password()
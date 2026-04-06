import random, string

class User:
    def __init__(self, uid, name, pwd):
        self.data = (uid, name, pwd)

try:
    uid = int(input("ID: "))
    name = input("Name: ")
    words = input("Enter words: ").split()

    if not words:
        raise ValueError("No words given")

    pwd = ''.join(random.sample(words, min(2, len(words))))
    pwd += str(random.randint(10, 99)) + random.choice("!@#$%")
    pwd = pwd.capitalize()

    while len(pwd) <= 8:
        pwd += random.choice(string.ascii_letters)

    print("Password:", pwd)

    user = User(uid, name, pwd)
    print("User Tuple:", user.data)

except Exception as e:
    print("Error:", e)
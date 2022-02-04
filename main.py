import string
import random

def passwordgen(length):
    a=list(string.ascii_lowercase)
    a.extend(list(string.ascii_uppercase))
    a.extend(list(string.punctuation))
    password=""
    for _ in range(length):
        password+=random.choice(a)
    return password

print(passwordgen(15))
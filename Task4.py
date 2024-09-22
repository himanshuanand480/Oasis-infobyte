import random
import string
length=int(input("Enter the length of password: "))
chars=string.ascii_letters
chars=chars+string.digits
chars=chars+string.punctuation
password=""
for i in  range(length):
    next_character=random.choice(chars)
    password=password+next_character
print("Password: ",password)

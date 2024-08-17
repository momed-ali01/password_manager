import random

letters_in_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_in_lowercase = "abcdefghijklmnopqrstuvwxyz"
special_keywords = '!?@#$%&_~'
numbers = "0123456789"

string = letters_in_uppercase + letters_in_lowercase + numbers + special_keywords
pass_length = 12

passw = "".join(random.sample(string, pass_length))

print("your password is: " + passw)

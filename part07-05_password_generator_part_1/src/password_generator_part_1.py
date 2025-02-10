# Write your solution here
from random import randint,sample
import string

def generate_password(length:int):
   lowercase_password = string.ascii_lowercase
   password_generated = sample(lowercase_password,length)
   return "".join(password_generated)

if __name__ == "__main__":

  for i in range(10):
    print(generate_password(8))
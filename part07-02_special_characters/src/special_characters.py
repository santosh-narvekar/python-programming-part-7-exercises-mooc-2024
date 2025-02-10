# Write your solution here
from string import ascii_letters
from string import punctuation

def separate_characters( my_string: str )->tuple:
  string1 = "".join( char for char in my_string if char in ascii_letters )
  string2 = "".join(char for char in my_string if char in punctuation)
  string3 = "".join(char for char in my_string if char not in ascii_letters and char not in punctuation )

  return (string1,string2,string3)

if __name__ == "__main__":
  parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
  print(parts[0])
  print(parts[1])
  print(parts[2])
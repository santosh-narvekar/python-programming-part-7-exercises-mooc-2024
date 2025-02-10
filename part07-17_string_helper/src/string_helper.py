# Write your solution here
from string import ascii_letters,digits,whitespace

def  change_case(orig_string: str):

  new_string = ""
  for char in orig_string:
    if char.islower():
      new_string += char.upper()
    else:
      new_string += char.lower()
  return new_string

def split_in_half(orig_string: str):
  split_index = len(orig_string) // 2 
  split_1 = orig_string[0: split_index]
  split_2 = orig_string[split_index:]
  return (split_1,split_2)

def remove_special_characters(orig_string: str):
  new_string = ""

  for char in orig_string:
    if char in ascii_letters or char in digits or char in whitespace :
      new_string += char
      
  return new_string

if __name__ == "__main__":
  print(change_case("Well hello there!"))
  split_in_half("Well hello there!")
  print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
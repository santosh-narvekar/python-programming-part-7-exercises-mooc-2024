# Write your solution here
import difflib

user_input = input("write text:")
user_input_list = user_input.split(" ")

correct_words = []

with open("wordlist.txt") as new_file:
  for word in new_file:
    word = word.replace("\n","")
    correct_words.append(word)

output_list = []
incorrect_words = []

for word in user_input_list:
  lowered_case_word = word.lower()
  if (lowered_case_word in correct_words):
    output_list.append(word)
  else:
    formatted_text = f"*{word}*"
    output_list.append(formatted_text)
    incorrect_words.append(word)

output_string = " ".join(output_list)

print(output_string)
print("suggestions:")

for word in incorrect_words:
  # word => string
  # correct_words []
  print(f"{word}: ",end="")
  suggested_words = difflib.get_close_matches(word,correct_words)
  for i,suggested_word in enumerate(suggested_words):
    print(f"{suggested_word}{", " if i != len(suggested_words) - 1 else "" }",end="")
  print()
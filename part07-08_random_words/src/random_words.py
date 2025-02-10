# Write your solution here
from random import randint

def words(n:int, beginning:str):
  words_found = [] 
  words_selected = []
  
  with open("words.txt") as new_file:
    for word in new_file:
      word = word.replace("\n","")
      if ( word.startswith(beginning) ):
        words_found.append(word)
  
  words_found = list(set(words_found))
  
  if n < len(words_found)  :
    for i in range(n):
      words_selected.append(words_found[randint(0, len(words_found) - 1 )])
  else:
    raise ValueError('Incorrect value provided')
  return words_selected

if __name__ == "__main__":
 
  word_list = words(7, "ca")
  for word in word_list:
    print(word)
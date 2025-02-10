# Write your solution here
from random import randint,sample,shuffle
import string

def generate_strong_password(length:int,numbers_to_include:bool,wild_characters_to_include:bool):
  lower_case_characters = string.ascii_lowercase
  numbers = list(range(0,9))
  wild_characters = [ "!","?","=","+","-","(",")","#" ]
  generated_password = sample(lower_case_characters,length)

  if not(numbers_to_include) and not(wild_characters_to_include):
    return "".join(generated_password)

  else:

    if numbers_to_include:
      # generating amount of time we want to change from 1 to length - 1
      run_through_loop_times = randint(1,length - 1)
      
      # looping through the generated random times and assigning the randomly generated numbers to
      # random positions of generated password

      for _ in range(run_through_loop_times):
        generated_password[ randint(0, length-1) ] = numbers[randint(0,len(numbers) - 1)]

    if wild_characters_to_include:
      # including positions of char indexes
      only_char_indexes = [] 

      for i,char in enumerate(generated_password):
        if isinstance(char,str):
          only_char_indexes.append(i)
      
      # shuffling the values
      shuffle(only_char_indexes)

      # taking the slice from 0 to random value from 1 to len(only_char_indexes) - 1
      slice_char_indexes = randint( 1, len(only_char_indexes) - 1 )
      only_char_indexes = only_char_indexes[0:slice_char_indexes]
      
      # taking the only_char_index values as index and assigning it random wild characters
      for i in only_char_indexes:
        generated_password[i] = wild_characters[randint(0,len(wild_characters) - 1)]
   
    return "".join(str(char) for char in generated_password)
  
if __name__ == "__main__":
  for i in range(10):
    print(generate_strong_password(20, True, True))
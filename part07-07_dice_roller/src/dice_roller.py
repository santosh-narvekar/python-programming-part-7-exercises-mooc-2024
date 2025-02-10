# Write your solution here
from random import choice,sample

def roll(die:str):

  if die == "A":
     value = sample([3,3,3,3,3,6],1)
     return value[0]
  
  if die == "B":
     value = sample([2,2,2,5,5,5],1)
     return value[0]

  if die == "C":
    value = sample([1, 4, 4, 4, 4, 4],1)
    return value[0]
  
def generate_Sample(die1):
  if die1 == "A":
    return [3, 3, 3, 3, 3, 6]
  
  if die1 == "B":
    return [2, 2, 2, 5, 5, 5]
  
  if die1 == "C":
    return [1, 4, 4, 4, 4, 4]
  
def play(die1: str, die2: str, times: int):
  ties = 0
  no_of_times_die1_won = 0
  no_of_times_die2_won = 0
  # AC CA BC CB AB BA CC BB AA
  # A > B > C > A
 
  if (die1 == "C" and die2 == "A" ) or (die1 =="B" and  die2 == "C") or (die1 == "A" and die2 == "B"): # CA , BC , AB
     # die1 is always greater than die2
     for _ in range(times):
       sample1 = sample(generate_Sample(die1),1)
       sample2 = sample(generate_Sample(die2),1)

       if sample1 > sample2:
         no_of_times_die1_won += 1
       else:
         no_of_times_die2_won += 1

  elif (die1 == "A" and die2 == "C" ) or (die1 =="C" and  die2 == "B") or (die1 == "B" and die2 == "A"): # AC , CB,BA
    # die1 is always less than die2
    for _ in range(times):
       sample1 = sample(generate_Sample(die1),1)
       sample2 = sample(generate_Sample(die2),1)

       if sample2 >= sample1:
         no_of_times_die2_won += 1
       else:
         no_of_times_die1_won += 1

  else: # CC,BB,AA
    # die1 is always equal to die2
    for _ in range(times):
      sample1 = sample(generate_Sample(die1), 1)
      sample2 = sample(generate_Sample(die2), 1)
      
      if sample1 > sample2:
         no_of_times_die1_won += 1
      elif sample2 <= sample1:
        no_of_times_die2_won += 1
      else:
         ties += 1
   
  return (no_of_times_die1_won,no_of_times_die2_won,ties)

if __name__ == "__main__":
  for i in range(20):
    print(roll("A"), " ", end="")
  
  print()
  for i in range(20):
    print(roll("B"), " ", end="")
  print()
  
  for i in range(20):
    print(roll("C"), " ", end="")

  result = play("A","C",1000)
  print(result)
  result = play("B","B",1000)
  print(result)
  
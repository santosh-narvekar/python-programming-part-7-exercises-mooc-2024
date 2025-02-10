# Write your solution here
from fractions import Fraction

def fractionate(amount:int) -> list:
  fractions_list = [] 
  cur_amount = 0

  while cur_amount < amount:
    fractions_list.append(Fraction(1,amount))
    cur_amount += 1
  return fractions_list

if __name__ == "__main__":
  for p in fractionate(3):
    print(p)

  print()

  print(fractionate(5))
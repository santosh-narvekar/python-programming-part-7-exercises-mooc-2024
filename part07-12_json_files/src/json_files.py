# Write your solution here
import json
def print_persons(filename:str):
 
  with open(filename) as my_file:
    data = my_file.read()
    
  students = json.loads(data)
  for student in students:
    print(f"{student["name"]} {student["age"]} years (",end="")
    for i,hobby in enumerate(student["hobbies"]):
      if i == len(student["hobbies"]) -1:
        print(hobby,end="")
      else:
        print(hobby,end=", ")
    print(")")

if __name__== "__main__":
  print_persons("file1.json")
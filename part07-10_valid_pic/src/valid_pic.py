# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
  # initializing all necessary variables
  markers_allowed = ["+","-","A"]
  check_control_character = "0123456789ABCDEFHJKLMNPRSTUVWXY"
  marker = pic[6]
  personal_identifier = pic[7:10]
  control_character = pic[10]
  
  # initializing all variables needed for date validation
  date_validation = True
  date_format = "%d%m%Y"
  check_date = pic[0:6] 
  
  year = "1800"

  if marker == "-":
    year = "1900"

  if marker == "A":
    year = "2000"
  
  day = check_date[0:2]
  month = check_date[2:4]
  full_year = year[0:2] + check_date[4:]
  date_to_check = day + month + full_year
  
  # verifying date in format
  try:
    datetime.strptime(date_to_check,date_format)
  except:
    date_validation = False

  index = int( check_date + personal_identifier ) % 31 

  if date_validation and marker in markers_allowed and control_character == check_control_character[index] and len(pic) < 12 :
    return True
  else:
    return False

if __name__ == "__main__":
  print(is_it_valid("230827-906F"))
  print(is_it_valid("120488+246L"))
  print(is_it_valid("310823A9877"))
  print(is_it_valid("080842-720N"))
  print(is_it_valid("290200-1239")) 
# Write your solution here
from datetime import datetime

birth_day = int(input("Day: "))
birth_month = int(input("Month: "))
birth_year = int(input("Year: "))
# 10-9-1979
new_millennium = datetime(2000,1,1) 
user_birth_date = datetime(birth_year,birth_month,birth_day) 

if user_birth_date < new_millennium:
  no_of_days =  new_millennium - user_birth_date
  print(f"You were {no_of_days.days - 1} days old on the eve of the new millennium.")
else:
  print(f"You weren't born yet on the eve of the new millennium.")
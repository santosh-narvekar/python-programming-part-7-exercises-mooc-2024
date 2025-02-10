# Write your solution here
from datetime import datetime,timedelta
file_name = input("Filename: ")
start_date = datetime.strptime(input("Starting date: "),"%d.%m.%Y")
days = input("How many days:")

print("Please type in screen time in minutes on each day (TV computer mobile):")

avg_minutes = 0
tot_minutes = 0
user_inputs = []
file_format_inputs = []
dates = []
start_date_format = start_date.strftime("%d.%m.%Y")
end_date_format = (start_date + timedelta(days = int(days) - 1)).strftime("%d.%m.%Y")

for day in range(int(days)):
  cur_date = (start_date + timedelta(days = day)).strftime("%d.%m.%Y")
  user_input = input(f"Screen time {cur_date}: ") 
  dates.append(cur_date)
  min_spend = user_input.split(" ") #[ 60,120,0 ]
  file_format_inputs.append("/".join(min_spend))
  for min in min_spend:
    if min != "0":
      user_inputs.append(int(min))

with open(file_name,"w") as new_file:
  new_file.write(f"Time period: {start_date_format}-{end_date_format}\n")

  new_file.write(f"Total minutes: {sum(user_inputs)}\n")      
  new_file.write(f"Average minutes: { (sum(user_inputs) / int(days)) }\n")

  for (i,date) in enumerate(dates):
    for formatted_inputs in file_format_inputs[i:]:
      new_file.write(f"{date}: {formatted_inputs}\n")
      break

print(f"Data stored in file {file_name}")
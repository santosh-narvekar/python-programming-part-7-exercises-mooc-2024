# Write your solution here
from datetime import datetime

def final_points():
  start_times = [] # [ ; ]
  students_tasks = { }
  
  with open("start_times.csv") as new_file:
    for start_time in new_file:
      start_time = start_time.replace("\n","")
      start_times.append(start_time.split(";"))

  with open("submissions.csv") as new_file:
    for submission in new_file:
      submission = submission.replace("\n","")
      submission = submission.split(";")

      # first access the start time of submission[0] 
      s_time = 0

      for start_time in start_times:
        if ( start_time[0] == submission[0] ):
          s_time = start_time[1]
          break
      
      # splitting up the start_time and end_time dates
      s_time = start_time[1].split(":")
      e_time = submission[3].split(":")
        
      # calculating time by using the date time object
      # using a experimental date 
      time1 = datetime(2021,6,30,int(s_time[0]),int(s_time[1]))
      time2 = datetime(2021,6,30,int(e_time[0]),int(e_time[1]))
      difference = abs(time2-time1)
  
      if difference.seconds <= 10800:

        submission_dict = {
             submission[1] : int(submission[2])
        }
        
        # check if key already exists in the student_tasks dictionary
        if submission[0] in students_tasks:
          # check if key already exists in the student dictionary
          if submission[1] in students_tasks[submission[0]]:
            # check if value for that key is less than current value
            if students_tasks[submission[0]][submission[1]] < int(submission[2]):
              # assign the new value to students key
              students_tasks[submission[0]][submission[1]] = int(submission[2])   
          else:
            # if key doesn't exist in students dictionary
            students_tasks[submission[0]][submission[1]] = int(submission[2]) 
          
        else:
          # if key doesn't exist in student tasks dictionary
          students_tasks[submission[0]] = submission_dict

  students_total_points = {}  
  
  for student_name,student_data in students_tasks.items():
    tot_val = 0
    for _,values in student_data.items():
      tot_val += values
    students_total_points[student_name] = tot_val

  return students_total_points

if __name__ == "__main__":
  print(final_points())
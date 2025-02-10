# Write your solution here
from datetime import datetime
def cheaters():
  
  start_times = []
  end_times = []

  with open("start_times.csv") as new_file:
    for start_time in new_file:
      start_time = start_time.replace("\n","")
      start_times.append(start_time.split(";"))

  with open("submissions.csv") as new_file:
    for end_time in new_file:
      end_time = end_time.replace("\n","")
      end_times.append(end_time.split(";"))
  
  cheaters_list = []
  
  # first running the start times array loop
  for start_time in start_times:
    # looking up the name for the start_time name 
    # while running end times loop

    for end_time in end_times:
      if ( end_time[0] == start_time[0] ):
        
        # splitting up the start_time and end_time dates
        s_time = start_time[1].split(":")
        e_time = end_time[3].split(":")
        
        # calculating time by using the date time object
        # using a experimental date 
        time1 = datetime(2021,6,30,int(s_time[0]),int(s_time[1]))
        time2 = datetime(2021,6,30,int(e_time[0]),int(e_time[1]))
        difference = abs(time2-time1)
        
        # comparing the difference in seconds 
        if difference.seconds > 10800:
          cheaters_list.append(end_time[0])
          break
  
  return cheaters_list

if __name__ == "__main__":
  print(cheaters())
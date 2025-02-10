# Write your solution here
import urllib.request
import json

def retrieve_all():
  new_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses ").read()
  all_courses = json.loads(new_request)
  
  active_courses = [ ( course["fullName"], course["name"],course["year"],sum(course["exercises"]) ) for course in all_courses if course["enabled"] ]

  return active_courses

def retrieve_course(course_name:str):
  new_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats ").read()
  course_weekly_data = json.loads(new_request)
  course_details = {}
  course_details["weeks"] = len(course_weekly_data)
  max_students_enrolled = course_weekly_data[list(course_weekly_data.keys())[0]]["students"]

  total_hours = 0
  total_exercises = 0

  for week_no in course_weekly_data:
    week_data = course_weekly_data[week_no]

    if week_data["students"] >=  max_students_enrolled :  
      max_students_enrolled = week_data["students"]

    total_hours += week_data["hour_total"]
    total_exercises += week_data["exercise_total"
                                 ]
  
  course_details["students"] = max_students_enrolled
  course_details["hours"] = total_hours
  course_details["hours_average"] = total_hours // max_students_enrolled
  course_details["exercises"] = total_exercises
  course_details["exercises_average"] = total_exercises // max_students_enrolled
  
  return course_details

if __name__ == "__main__":
  print(retrieve_all())
  print(retrieve_course("docker2019"))
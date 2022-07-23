import random

# #List comprehention

# numbers=[1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)


# range_list = [num*2 for num in range (1,5)]
# print(range_list)

# names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# short_names=[name for name in names if len(name)<=4]
# print(short_names)

# cap_names=[name.upper() for name in names if len(name)>4]
# print(cap_names)

# #Dictionary comprehention
# student_scores={student:random.randint(0,100) for student in names}
# print(student_scores)

# passed_students={student:grade for (student,grade) in student_scores.items() if grade>59}
# print(passed_students)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f={day:((temp*9/5)+32) for (day,temp) in weather_c.items()}



print(weather_f)
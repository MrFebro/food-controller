from functions_lib_febro import date_en
from datetime import datetime
from datetime import timedelta
from math import floor as fl
# FUNCTIONS
def main_title():
  print('')
  print('-=-' * 15)
  print('GOLDEN ARROW - Project Deadline Controller 1.0')
  print('')
  print('This will allow me to know the deadline of my Project and insert infos into Progress App')
  print('-=-' * 15)



main_title()
print('')
list_type_mile = ['Lesson', 'Task']
lenl = len(list_type_mile) + 1 # this + 1 is required because otherwise it will be display only 1 option out of 2 of them
cont = 0
print('TYPES OF MILESTONE/STEP:')
for n in range(1, lenl): 
  print(f'[{n}] {list_type_mile[cont]}')
  cont += 1
user_step = ' '

while user_step not in range(1, lenl):
  user_step = int(input('Option here: '))

user_type = list_type_mile[user_step - 1].upper()
step_total = int(input('In TOTAL, how many {}S will you have along the way? '.format(user_type)))
steps_day = int(input('How many {}S are you willing to carry out DAILY, Febro? '.format(user_type)))
total_days = fl(step_total // steps_day)
res_days = step_total % steps_day
if res_days == 0:
  res_days = 'NONE'
#date management
# today for START
date_start = datetime.today()
# finish date:
date_finish = datetime.today() + timedelta(days=total_days - 1) #- 1 COUNTING TODAY
print('RESULT')
print(f'This Project will...')
print(f'START (Counting today): {date_en(date_start)}')
print('')
print(f'FINISH: {date_en(date_finish)}')
print('')
print(f'You will have {res_days} ADDITIONAL {user_type}S')
print(f'Then, you will start off the project with  {total_days + res_days} {user_type}S TODAY')
print(f'The rest is {total_days} per day')
print('Let´s succeed in doing this, Mr. Febro!')
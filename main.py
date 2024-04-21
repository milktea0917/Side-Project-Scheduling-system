import logging
import os
import pandas as pd
from loading_employee import employee
from arranging_algo import arranging_version2, absent_pleasure_test

assert os.path.exists("../SideProject/employee.xlsx")==True
employee_xlsx = pd.read_excel(r"../SideProject/employee.xlsx")
# print(employee_xlsx)

""" 
<<<<<<< HEAD
# Create worker_list by loading employee.xlsx 
1. worker_list: list of employee(class)
2. employee_feature: list of employee's feature
2. weekday_worker_list: list of weekday workers
3. weekend_worker_list: list of weekend workers
=======
1. Create worker_list by loading employee.xlsx 
2. worker_list: list of employee(class)
<<<<<<< HEAD
>>>>>>> parent of 6e4753d (2024.04.20)
=======
>>>>>>> parent of 6e4753d (2024.04.20)
"""
worker_list = []
for i in range(len(employee_xlsx)):
    employee_feature = employee_xlsx.loc[i].tolist()
<<<<<<< HEAD
<<<<<<< HEAD
    employee_feature = employee(employee_feature)
    worker_list.append(employee_feature)
weekday_worker_list, weekend_worker_list = split_weekday_weekend(worker_list)

# getting out parameters
"""
# Getting hyperparameters
1. year, month: for calendar.monthcalendar
2. weekday_pos,  weekend_pos: position setting
"""
year, month, weekday_pos, weekend_pos = setting_xlsx.iloc[0]

working_daylist = calendar.monthcalendar(year, month) # list of list 

"""
1. week: 1~7 (Mon. ~ Sun.)
2. date: 0~28,29,30,31,
"""
for i in range(len(working_daylist)):

    if i == 1:
        break

    for week, date in enumerate(working_daylist[i]):

        if date == 0: # if not in this month 
            continue
        elif week<5 : # if weekdays
            print(f"今天{month}/{date}，星期{week+1}:")
            arranging(weekday_pos, weekday_worker_list, date)
        else: # if weekends
            print(f"今天{month}/{date}，星期{week+1}:")
            arranging(weekend_pos, weekend_worker_list, date)
=======
    employee_i = employee(employee_feature)
    worker_list.append(employee_i)

"""
ToDo:
1. Write Something to control days, month, absent, holidays, weekdays
2. 比例排班
"""

=======
    employee_i = employee(employee_feature)
    worker_list.append(employee_i)

"""
ToDo:
1. Write Something to control days, month, absent, holidays, weekdays
2. 比例排班
"""

>>>>>>> parent of 6e4753d (2024.04.20)
### 請假壓力測試 ### 
# 平常的話，absent設為0即可
work_space = 8
times = 1
absent_number = 0
<<<<<<< HEAD
absent_pleasure_test(work_space, worker_list, times, absent_number)
>>>>>>> parent of 6e4753d (2024.04.20)
=======
absent_pleasure_test(work_space, worker_list, times, absent_number)
>>>>>>> parent of 6e4753d (2024.04.20)

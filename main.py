import os
import pandas as pd
from loading_employee import employee, split_weekday_weekend
from arranging_algo import arranging
import calendar

assert os.path.exists("../SideProject/employee.xlsx")==True
employee_xlsx = pd.read_excel(r"../SideProject/employee.xlsx")
setting_xlsx = pd.read_excel(r"../SideProject/setting.xlsx")

""" 
1. Create worker_list by loading employee.xlsx 
2. worker_list: list of employee(class)
3. weekday_worker_list: list of weekday workers
4. weekend_worker_list: list of weekend workers
"""
worker_list = []
for i in range(len(employee_xlsx)):
    employee_feature = employee_xlsx.loc[i].tolist()
    employee_i = employee(employee_feature)
    worker_list.append(employee_i)

weekday_worker_list, weekend_worker_list = split_weekday_weekend(worker_list)

# getting out parameters
year, month, weekday_pos, weekend_pos = setting_xlsx.iloc[0]

working_daylist = calendar.monthcalendar(year, month) # list of list 

for i in range(len(working_daylist)):

    for day, content in enumerate(working_daylist[i]):

        if content == 0: # if not in this month 
            continue
        elif day<5 : # if weekdays
            print(f"今天{month}/{content}，星期{day+1}:")
            arranging(weekday_pos, weekday_worker_list, absent_number=0)
        else: # if weekends
            print(f"今天{month}/{content}，星期{day+1}:")
            arranging(weekend_pos, weekend_worker_list, absent_number=0)

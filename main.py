import logging
import os
import pandas as pd
from loading_employee import employee, split_weekday_weekend
from arranging_algo import arranging
from counter import showing_arranging_results
import calendar

assert os.path.exists("../SideProject/employee.xlsx")==True
employee_xlsx = pd.read_excel(r"../SideProject/employee.xlsx")
setting_xlsx = pd.read_excel(r"../SideProject/setting.xlsx")

""" 
# Create worker_list by loading employee.xlsx 
1. worker_list: list of employee(class)
2. employee_feature: list of employee's feature
2. weekday_worker_list: list of weekday workers
3. weekend_worker_list: list of weekend workers
"""
worker_list = []
for i in range(len(employee_xlsx)):
    employee_feature = employee_xlsx.loc[i].tolist()
    employee_feature = employee(employee_feature)
    worker_list.append(employee_feature)
weekday_worker_list, weekend_worker_list = split_weekday_weekend(worker_list)

# getting out parameters
"""
# Getting hyperparameters
1. year, month: for calendar.monthcalendar
2. weekday_pos,  weekend_pos: weekday_pos(Mon. ~ Fri.) weekend_pos(Sat.~ Sun.)
3. if single_day==1: arranging only one single day; single_day is default to 0
4. weekday_weekend: 1 for weekday, 2 for weekend, 0 for default
5. single_date: the date want to arrange alone
"""
year, month, weekday_pos, weekend_pos, if_single_day, weekday_weekend, single_date, rest_date = setting_xlsx.iloc[0]
working_daylist = calendar.monthcalendar(year, month) # list of list 

"""
1. week: 1~7 (Mon. ~ Sun.)
2. date: 0~28,29,30,31,
3. weekday_counter: to show weekday's arranging
3. weekend_counter: to show weekend's arranging
"""
weekday_counter = [0] * len(weekday_worker_list)
weekend_counter = [0] * len(weekend_worker_list)

if if_single_day == 0:
    for i in range(len(working_daylist)):
        for week, date in enumerate(working_daylist[i]):
            if date == 0 : # if not in this month 
                continue
            if date == rest_date:
                print(f"今天{month}/{date}，星期{week+1}，哀有~今天休假\n")
                continue
            elif week<5 : # if weekdays
                print(f"今天{month}/{date}，星期{week+1}:")
                arranging_list, already_pick = arranging(weekday_pos, weekday_worker_list, date)
                weekday_counter = [sum(x) for x in zip(weekday_counter, already_pick)]
            else: # if weekends
                print(f"今天{month}/{date}，星期{week+1}:")
                arranging_list, already_pick = arranging(weekend_pos, weekend_worker_list, date)
                weekend_counter = [sum(x) for x in zip(weekend_counter, already_pick)]
else: 
    if weekday_weekend ==1:
        print(f"進行單天的平日排班")
        arranging_list, already_pick = arranging(weekday_pos, weekday_worker_list, single_date)
        weekday_counter = [sum(x) for x in zip(weekday_counter, already_pick)]
    elif weekday_weekend ==2:
        print(f"進行單天的假日排班")
        arranging_list, already_pick = arranging(weekend_pos, weekend_worker_list, single_date)
        weekend_counter = [sum(x) for x in zip(weekend_counter, already_pick)]
    else:
        logging.error(f"weekday_weekend went wrong from setting.xlsx.")

showing_arranging_results(worker_list, weekday_worker_list, weekend_worker_list, weekday_counter, weekend_counter)

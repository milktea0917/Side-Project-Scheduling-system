import os
import pandas as pd
from loading_employee import employee
from arranging_algo import arranging_version2, absent_pleasure_test

assert os.path.exists("../SideProject/employee.xlsx")==True
employee_xlsx = pd.read_excel(r"../SideProject/employee.xlsx")
# print(employee_xlsx)

""" 
1. Create worker_list by loading employee.xlsx 
2. worker_list: list of employee(class)
"""
worker_list = []
for i in range(len(employee_xlsx)):
    employee_feature = employee_xlsx.loc[i].tolist()
    employee_i = employee(employee_feature)
    worker_list.append(employee_i)

"""
ToDo:
1. Write Something to control days, month, absent, holidays, weekdays
2. 比例排班
"""

### 請假壓力測試 ### 
# 平常的話，absent設為0即可
work_space = 8
times = 1
absent_number = 0
absent_pleasure_test(work_space, worker_list, times, absent_number)
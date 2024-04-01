import os
import pandas as pd
import random
from loading_employee import employee
from arranging_algo import arranging_version1


"""
ToDo:
load employee by excel
"""

assert os.path.exists("../SideProject/employee.xlsx")==True
employee_xlsx = pd.read_excel(r"../SideProject/employee.xlsx")
print(employee_xlsx)

# self.ability_list = [cook, bread, noodle_fry, noodle_ya , pack, order, drink, korea_dishes] 

# 假日
Hsu =       employee("Hsu", 10,0,0,0,0,0,0,0)
ET =        employee("ET", 0,10,0,0,0,0,0,0)
# 內場
Lan =       employee("Lan", 0,0,7,10,0,0,0,0)
Lucy =      employee("Lucy", 0,0,10,8,9,0,0,7)
May_Jiao =  employee("May_Jiao", 0,0,9,7,1,0,2,8)
Rain_Stop = employee("Rain_Stop", 0,0,8,9,8,8,10,10)
# 外場

May_Jun =   employee("May_Jun", 0,0,0,6,7,9,10,6)
Zhe =       employee("Zhe", 0,0,0,0,0,10,9,6)
May_Chi =   employee("May_Chi", 0,0,0,0,10,5,6,6)
Jay =       employee("Jay", 0,0,0,0,2,6,9,3)
Jia_Lin =   employee("Jia_Lin", 0,0,0,0,8,8,10,3)

# 平日
Cai_Min =   employee("Cai_Min", 0,0,0,0,1,8,10,3)
Shu_Han =   employee("Shu_Han", 0,0,0,0,1,8,10,3)

"""
ToDo:
Write Something to control days, month, absent, holidays, weekdays
"""
work_space = 8
boss_list = [Hsu, ET]
worker_list = [Lan, Lucy, May_Jiao, Rain_Stop, May_Jun, Zhe, May_Chi, Jay, Jia_Lin]
results = arranging_version1(work_space, worker_list)

print(f"今天可以上班的人:{len(worker_list+boss_list)}")
print(f"煎台:{results[0]}，麵包:{results[1]}，煮麵:{results[2]}，雅：{results[3]}，\
      包餐：{results[4]}，點餐：{results[5]}，飲料：{results[6]}，韓式：{results[7]}")
print(f" ")

### 測資 ###
# print(f"###來點好玩的，假設今天隨機兩個人請假###")
# for i in range(8):
#     worker_list_new = random.sample(worker_list,k=(len(worker_list)-2))
#     absent = set(worker_list)-set(worker_list_new)
#     print(f"今天請假人數: {len(absent)}")
#     for j in absent:
#         print(f"請假: {j.name}")

#     worker_list_new = worker_list_new + boss_list
#     temp_results = arranging_version1(work_space, worker_list_new)
#     print(f"今天可以上班的人:{len(worker_list)-2}")
#     print(f"煎台:{temp_results[0]}，麵包:{temp_results[1]}，煮麵:{temp_results[2]}，雅：{temp_results[3]}，\
#       包餐：{temp_results[4]}，點餐：{temp_results[5]}，飲料：{temp_results[6]}")
#     print(f"####")
#     print(f" ")

    
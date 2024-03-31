import random
from loading_employee import employee
from arranging_algo import arranging_version1


"""
ToDo:
This will be replace by loading excel file.
"""
# self.ability_list = [noodle_fry, noodle_ya , pack, order, drink, korea_dishes]

# 假日
# 內場
Lan = employee("Lan", 3,5,0,0,0,0)
Lucy = employee("Lucy", 5,3,4,0,0,0)
May_Jiao = employee("May_Jiao", 2,5,0,0,0,0)
Rain_Stop = employee("Rain_Stop", 4,4,0,0,0,0)
# 外場

May_Jun = employee("May_Jun", 0,2,3,4,4,5)
Zhe = employee("Zhe", 0,0,2,5,4,0)
May_Chi = employee("May_Chi", 0,0,10,0,0,0)
Jay = employee("Jay", 0,0,1,4,5,0)
Jia_Lin = employee("Jia_Lin", 0,0,5,4,4,0)

# 平日
Cai_Min = employee("Cai_Min", 0,0,0,3,4,0)
Shu_Han = employee("Shu_Han", 0,0,0,4,4,0)

"""
ToDo:
Write Something to control days, month, absent, holidays, weekdays
"""
work_space = 6
worker_list = [Lan, Lucy, May_Jiao, Rain_Stop, May_Jun, Zhe, May_Chi, Jay, Jia_Lin]
results = arranging_version1(work_space, worker_list)

print(f"今天可以上班的人:{len(worker_list)}")
print(f"煮麵:{results[0]}，雅：{results[1]}，包餐：{results[2]}，點餐：{results[3]}，飲料：{results[4]}，韓式：{results[5]}")

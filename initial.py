import os
import pandas as pd

from loading_employee import Employee

import calendar

class initial: 

    def CheckPath(self): # "讀出 1. 員工表 2. 設定表"

        cwd = os.getcwd()
        assert os.path.exists(cwd)==True

        employee_xlsx = os.path.join(cwd, "employee.xlsx")
        employee_xlsx = pd.read_excel(employee_xlsx)
        
        setting_xlsx = os.path.join(cwd, "setting.xlsx")
        setting_xlsx = pd.read_excel(setting_xlsx)

        result_path = os.path.join(cwd, '排班結果.txt')
        if os.path.exists(result_path)==True: # 如果已經有產生，重新生成一個空白的
            f = open('排班結果.txt', 'w')
        
        return employee_xlsx, setting_xlsx
    
    def CreateWorker(self, employee_xlsx): # "分出 1. 平日班 2. 假日班"
        """ 
        分 平日班 假日班
        # Create worker_list by loading employee.xlsx 
        1. total_worker_list: list of employee(class)
        2. employee_feature: list of employee's feature
        2. weekday_worker_list: list of weekday workers
        3. weekend_worker_list: list of weekend workers
        """
        total_worker_list = []
        for i in range(len(employee_xlsx)):
            employee_feature = employee_xlsx.loc[i].tolist() # 讀 一個人 的 資料
            employee_feature = Employee(employee_feature) # 建 屬於一個人 的 class
            total_worker_list.append(employee_feature) # 建每一個人的狀態，所以會變成 "list of 員工"

        weekday_worker_list, weekend_worker_list = Employee.SplitWeekdayWeekend(total_worker_list) # "分出 1. 平日班 2. 假日班"
        
        return total_worker_list, weekday_worker_list, weekend_worker_list

    def LoadSettings(self, setting_xlsx):
        """
        讀 設定參數
        # Getting hyperparameters
        1. year, month: for calendar.monthcalendar
        2. weekday_pos,  weekend_pos: weekday_pos(Mon. ~ Fri.) weekend_pos(Sat.~ Sun.)
        3. if single_day==1: arranging only one single day; single_day is default to 0
        4. weekday_weekend: 1 for weekday, 2 for weekend, 0 for default
        5. single_date: the date want to arrange alone
        """
        year, month, weekday_pos, weekend_pos, if_single_day, weekday_weekend, single_date, rest_date = setting_xlsx.iloc[0]

        """
        將 calendar 設成以星期天開頭
        初始化 每個人上班的計數器
        1. week: 7~6 (Sun. ~ Sat.)
        2. date: 0~28,29,30,31,
        3. weekday_counter: to show weekday's arranging
        3. weekend_counter: to show weekend's arranging
        """
        calendar.setfirstweekday(calendar.SUNDAY)
        workday_list = calendar.monthcalendar(year, month) # list of list 

        return workday_list, year, month, weekday_pos, weekend_pos, if_single_day, weekday_weekend, single_date, rest_date 

def WorkdayCount(weekday_worker_list, weekend_worker_list): # "用來統計大家這個月上多少班"

    # "用兩條list區隔開，之後用成一個變數也可以"
    weekday_counter = [0] * len(weekday_worker_list)
    weekend_counter = [0] * len(weekend_worker_list)

    return weekday_counter, weekend_counter

def MergingArrangingResults(worker_list, counter , arranging_dictionary): # "將'平日班'、'假日班'的結果寫進dictionary"
        
        assert len(worker_list) == len(counter)
        
        # "直接把統計過的數字加到屬於那個人的 value裡面"
        for i in range(len(worker_list)):
            temp_name = worker_list[i].name
            arranging_dictionary[temp_name] = arranging_dictionary[temp_name] + counter[i]
        
        return arranging_dictionary
    
def ShowEveryoneWorkcount(worker_list, weekday_worker_list, weekend_worker_list, weekday_counter, weekend_counter): # "將'平日班'跟'假日班'一起送給merging_arranging_results做統計"
    
    # "dictionary initialize"
    arranging_dictionary = {}
    for i in range(len(worker_list)):
        arranging_dictionary[worker_list[i].name] = 0

    # "合併兩次dictionary的結果"
    arranging_dictionary = MergingArrangingResults(weekday_worker_list, weekday_counter, arranging_dictionary)
    arranging_dictionary = MergingArrangingResults(weekend_worker_list, weekend_counter, arranging_dictionary)

    # "print"
    for i in range(len(worker_list)):
        print(f"{worker_list[i].name} 這個月上班 {arranging_dictionary[worker_list[i].name]} 天。")

    try:
        with open("排班結果.txt", 'a') as f:
            f.write("\n")
            for i in range(len(worker_list)):
                f.write(f"{worker_list[i].name} 這個月上班： {arranging_dictionary[worker_list[i].name]} 天。\n") 
    except:
        pass


import pandas as pd

class CreatingXlsx():

    def __init__(self):
        self.data = {}

    def WriteDF(self, arranging_list, already_pick, date, week, week_count, month): # ToDo
        
        self.data[month,date] = arranging_list
        print(self.data)

    def DFtoExcel(self): # ToDo
        # 將 DataFrame 寫入新的 Excel 文件
        self.df = pd.DataFrame(self.data)
        self.df.to_excel("排班結果.xlsx", index=True)

    def DFtoTXT(self, arranging_list, date, week, month):
        
        if week == 6:
            space_flag = True
        else:
            space_flag = False
        
        try:
            with open("排班結果.txt", 'a') as f:
                if week==0:
                    f.write(f"{month}/{date}  星期7, 今天上班：{arranging_list} \n")    
                else:
                    f.write(f"{month}/{date}  星期{week}, 今天上班：{arranging_list} \n")
                if space_flag: 
                    f.write("\n")
        except:
            print(f"something went wrong")
        finally:
            f.close()

    def ShowDailyResult(self, work_space, arranging_list):
        if work_space == 8:
            print(f"煎台:{arranging_list[0]}，麵包:{arranging_list[1]}，煮麵:{arranging_list[2]}，雅：{arranging_list[3]}，\
            包餐：{arranging_list[4]}，點餐：{arranging_list[5]}，飲料：{arranging_list[6]}，機動：{arranging_list[7]}\n")
        elif work_space == 7:
            print(f"煎台:{arranging_list[0]}，麵包:{arranging_list[1]}，煮麵:{arranging_list[2]}，雅：{arranging_list[3]}，\
            包餐：{arranging_list[4]}，點餐：{arranging_list[5]}，飲料：{arranging_list[6]}\n")
        elif work_space == 3:
            print(f"煎台:{arranging_list[0]}，麵包:{arranging_list[1]}，\
                機動:{arranging_list[2]}\n")
        else:
            print(f"煎台:{arranging_list[0]}，麵包:{arranging_list[1]}，\
                煮麵:{arranging_list[2]}，機動：{arranging_list[3]} \n")
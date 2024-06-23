import argparse
from initial import initial
import logging
from arranging_algo import Arranging
from reporter import WorkdayCount, CreatingXlsx, ShowEveryoneWorkcount

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    start = initial()
    employee_xlsx, setting_xlsx = start.CheckPath()

    total_worker_list, weekday_worker_list, weekend_worker_list = start.CreateWorker(employee_xlsx)
    weekday_counter, weekend_counter = WorkdayCount(weekday_worker_list, weekend_worker_list)
    workday_list, year, month, weekday_pos, weekend_pos, if_single_day, weekday_weekend, single_date, rest_date = start.LoadSettings(setting_xlsx)

    parser.add_argument("-year", default=year, type=int) 
    parser.add_argument("-month", default=month, type=int)

    # 平日班、假日班 位置
    parser.add_argument("-weekday_pos", default=weekday_pos, type=int)
    parser.add_argument("-weekend_pos", default=weekend_pos, type=int)

    # 如果我要單天排班，排哪一天
    parser.add_argument("-if_single_day", default=if_single_day, type=bool)
    parser.add_argument("-single_date", default=single_date, type=int)

    parser.add_argument("-weekday_weekend", default=weekday_weekend, type=int) # 控制假日平日排班
    parser.add_argument("-rest_date", default=rest_date, type=list) # 店休
    parser.add_argument("-workday_list", default=workday_list, type=list) # 這個月的實際狀況，list of list , from calendar

    args = parser.parse_args()

    ReportXlsx = CreatingXlsx()

    if if_single_day == 0:
        for week_count in range(len(args.workday_list)):
            for week, date in enumerate(workday_list[week_count]):
                if date == 0 : # if not in this month 
                    continue
                if date == rest_date:
                    # print(f"今天{month}/{date}，星期{week}，哀有~今天休假\n")
                    continue
                elif 0<week<6 : # if weekdays
                    # print(f"今天{month}/{date}，星期{week}:")
                    arranging_list, already_pick = Arranging(ReportXlsx, weekday_pos, weekday_worker_list, date, week, month)
                    weekday_counter = [sum(x) for x in zip(weekday_counter, already_pick)]
                else: # if weekends
                    arranging_list, already_pick = Arranging(ReportXlsx, weekend_pos, weekend_worker_list, date, week, month)
                    weekend_counter = [sum(x) for x in zip(weekend_counter, already_pick)]
    else: 
        if weekday_weekend ==1:
            print(f"進行單天的平日排班")
            arranging_list, already_pick = Arranging(weekday_pos, weekday_worker_list, single_date)
            weekday_counter = [sum(x) for x in zip(weekday_counter, already_pick)]
        elif weekday_weekend ==2:
            print(f"進行單天的假日排班")
            arranging_list, already_pick = Arranging(weekend_pos, weekend_worker_list, single_date)
            weekend_counter = [sum(x) for x in zip(weekend_counter, already_pick)]
        else:
            logging.error(f"weekday_weekend went wrong from setting.xlsx.")

    # ReportXlsx.DFtoExcel() # ToDo
    ShowEveryoneWorkcount(total_worker_list, weekday_worker_list, weekend_worker_list, weekday_counter, weekend_counter)
    

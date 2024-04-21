import logging
class employee: 
    def __init__(self,input_list):
        
        """
        cook:                 煎台
        bread:                麵包
        noodle_fry:           煮麵+炸物
        noodle_ya:            雅+撈
        pack:                 包餐
        order:                點餐
        drink:                飲料
        flexible:             機動
        weekday/weekend/both: 1, 2, 3
        absent: string or nan(float)
        precentage: a precentage to control the arranging total amounts
        """
        self.name = input_list[0]
        self.ability_list = input_list[1:9]
        self.pt_time = input_list[9]
        if isinstance(input_list[10], str): # check the variable type
            self.absent_time = input_list[10].split(',')
        else: 
            self.absent_time = [0]
        
        # just in case 
        # print(f"self.name: {self.name}")
        # print(f"self.ability_list: {self.ability_list}")
        # print(f"self.pt_time: {self.pt_time}")
        # print(f"self.absent_time: {self.absent_time}")

def split_weekday_weekend(worker_list):
    weekday_worker_list = []
    weekend_worker_list = []
    for i in range(len(worker_list)): # ability_list[-2] = weekday/weekend/both

        if worker_list[i].pt_time == 1:
            weekday_worker_list.append(worker_list[i])
        elif worker_list[i].pt_time == 2:
            weekend_worker_list.append(worker_list[i])
        elif worker_list[i].pt_time == 3:
            weekday_worker_list.append(worker_list[i])
            weekend_worker_list.append(worker_list[i]) 
        else:
            logging.error(f"something went wrong in pt_time.")
        
    return weekday_worker_list, weekend_worker_list
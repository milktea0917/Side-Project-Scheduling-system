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
        weekday/weekend/both: 0, 1, 2
        """
        self.name = input_list[0]
        self.ability_list = input_list[1:] 

def split_weekday_weekend(worker_list):
    weekday_worker_list = []
    weekend_worker_list = []
    for i in range(len(worker_list)):

        if worker_list[i].ability_list[-1] == 1:
            weekday_worker_list.append(worker_list[i])
        elif worker_list[i].ability_list[-1] == 2:
            weekend_worker_list.append(worker_list[i])
        else:
            weekday_worker_list.append(worker_list[i])
            weekend_worker_list.append(worker_list[i])
        
    return weekday_worker_list, weekend_worker_list
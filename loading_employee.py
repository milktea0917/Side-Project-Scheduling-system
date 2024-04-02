class employee: 
    def __init__(self,input_list):
        
        """
        cook:         煎台
        bread:        麵包
        noodle_fry:   煮麵+炸物
        noodle_ya:    雅+撈
        pack:         包餐
        order:        點餐
        drink:        飲料
        korea_dishes: 韓式
        """
        self.name = input_list[0]
        self.ability_list = input_list[1:] 
class employee: # open version
    def __init__(self,name,cook,bread,noodle_fry,noodle_ya,pack,order,drink,korea_dishes):
        
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
        self.name = name
        self.ability_list = [cook, bread, noodle_fry, noodle_ya , pack, order, drink, korea_dishes] 
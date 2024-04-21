import logging
def check_absent(date, worker_list):

    already_pick = []

    for i in range(len(worker_list)):

        if date in worker_list[i].absent_time:
            print(f"{worker_list[i].name}今天請假. \n")
            already_pick.append(i)

    return already_pick
def arranging_algo(work_space, worker_list, date):

    """
    ToDo: 
        1. arranging precentage
        2. pack to .exe
    """
    
    """
    variable explaination:
        1. arranging_list: final return
        2. already_pick: not to pick the same person
        3. work_space: how many jobs is there in the kitchen
        4. worker_list: list with employee(class)
        5. if work_space == 4: workday, else: weekend
    """
    arranging_list = []
    already_pick = []

    if work_space == 4: # if weekday
        already_pick = check_absent(str(date), worker_list)
        for i in range(work_space): 

            if i == 0 or 1 or 2 or 7: # cook, bread, noodle, flexible
                candidate_index = -9999
                current_max = -9999

                for j in range(len(worker_list)):
                    if j in already_pick: # one person for one workspace
                        continue
                    if (current_max < worker_list[j].ability_list[i]):
                        current_max = worker_list[j].ability_list[i]
                        candidate_index = j

                arranging_list.append(worker_list[candidate_index].name)
                already_pick.append(candidate_index)

    else: # if weekday

        already_pick = check_absent(str(date), worker_list)
        for i in range(work_space): 
            candidate_index = -9999
            current_max = -9999

            for j in range(len(worker_list)):
                if j in already_pick: # one person for one workspace
                    continue
                if (current_max < worker_list[j].ability_list[i]):
                    current_max = worker_list[j].ability_list[i]
                    candidate_index = j

            arranging_list.append(worker_list[candidate_index].name)
            already_pick.append(candidate_index)

    return arranging_list

def arranging(work_space, worker_list, date):

    # "make sure workers' status"
    # if absent_number>0:
    #     print(f"### 今天{absent_number}人請假 ###")
    # # since the first of two employee are boss and boss's wife
    # worker_list_new = random.sample(worker_list[2:],k=(len(worker_list[2:])-absent_number))
    # absent = set(worker_list[2:])-set(worker_list_new)
    # for j in absent:
    #     print(f"請假: {j.name}")
    # print(f"今天可以上班的人:{len(worker_list_new+worker_list[:2])}")
    # temp_results = arranging_algo(work_space, worker_list_new+worker_list[:2])

    "Start Runing"
    temp_results = arranging_algo(work_space, worker_list, date)
    if work_space == 8:
        print(f"煎台:{temp_results[0]}，麵包:{temp_results[1]}，煮麵:{temp_results[2]}，雅：{temp_results[3]}，\
        包餐：{temp_results[4]}，點餐：{temp_results[5]}，飲料：{temp_results[6]}，機動：{temp_results[7]}\n")
    else:
        print(f"煎台:{temp_results[0]}，麵包:{temp_results[1]}，\
              煮麵:{temp_results[2]}，機動：{temp_results[3]} \n")

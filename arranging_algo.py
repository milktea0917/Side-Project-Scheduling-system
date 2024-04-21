<<<<<<< HEAD
import logging
def check_absent(date, worker_list):

    already_pick = []

    for i in range(len(worker_list)):

        if date in worker_list[i].absent_time:
            logging.info(f"{worker_list[i].name}今天請假. \n")
            already_pick.append(i)

    return already_pick
def arranging_algo(work_space, worker_list, date):
=======
import random
def arranging_version2(work_space, worker_list):
<<<<<<< HEAD
>>>>>>> parent of 6e4753d (2024.04.20)
=======
>>>>>>> parent of 6e4753d (2024.04.20)

    """
    version explaination:
        1. This version is very value at xlsx's scoring! 

    ToDo: 
<<<<<<< HEAD
<<<<<<< HEAD
        0. single day arranging
        1. arranging precentage
        2. pack to .exe
=======
        1. Let extra favor added. eg. Lan + May is wellcome to appear together.
>>>>>>> parent of 6e4753d (2024.04.20)
=======
        1. Let extra favor added. eg. Lan + May is wellcome to appear together.
>>>>>>> parent of 6e4753d (2024.04.20)
    """
    
    """
    variable explaination:
        1. arranging_list: final return
        2. already_pick: not to pick the same person
        3. work_space: how many jobs is there in the kitchen
        4. worker_list: list with employee(class)
    """

    arranging_list = []
    already_pick = []
    for i in range(work_space): 

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        candidate_index = 0
        current_max = 0
        for j in range(len(worker_list)):

            if j in already_pick: # since we can't pick the same person for two workspace, that is too hard.
                continue
            if (current_max < worker_list[j].ability_list[i]):
                current_max = worker_list[j].ability_list[i]
                candidate_index = j
            else:
                pass

        arranging_list.append(worker_list[candidate_index].name)
        already_pick.append(candidate_index)

    return arranging_list

def absent_pleasure_test(work_space, worker_list, times, absent_number):
    print(f"###來點好玩的，假設今天隨機兩個人請假###")
    for i in range(times):
        # since the first of two employee are boss and boss's wife
        worker_list_new = random.sample(worker_list[2:],k=(len(worker_list[2:])-absent_number))
        absent = set(worker_list[2:])-set(worker_list_new)
        print(f"今天請假人數: {len(absent)}")
        for j in absent:
            print(f"請假: {j.name}")

        temp_results = arranging_version2(work_space, worker_list_new+worker_list[:2])
        print(f"今天可以上班的人:{len(worker_list_new+worker_list[:2])}")
>>>>>>> parent of 6e4753d (2024.04.20)
=======
        candidate_index = 0
        current_max = 0
        for j in range(len(worker_list)):

            if j in already_pick: # since we can't pick the same person for two workspace, that is too hard.
                continue
            if (current_max < worker_list[j].ability_list[i]):
                current_max = worker_list[j].ability_list[i]
                candidate_index = j
            else:
                pass

        arranging_list.append(worker_list[candidate_index].name)
        already_pick.append(candidate_index)

    return arranging_list

def absent_pleasure_test(work_space, worker_list, times, absent_number):
    print(f"###來點好玩的，假設今天隨機兩個人請假###")
    for i in range(times):
        # since the first of two employee are boss and boss's wife
        worker_list_new = random.sample(worker_list[2:],k=(len(worker_list[2:])-absent_number))
        absent = set(worker_list[2:])-set(worker_list_new)
        print(f"今天請假人數: {len(absent)}")
        for j in absent:
            print(f"請假: {j.name}")

        temp_results = arranging_version2(work_space, worker_list_new+worker_list[:2])
        print(f"今天可以上班的人:{len(worker_list_new+worker_list[:2])}")
>>>>>>> parent of 6e4753d (2024.04.20)
        print(f"煎台:{temp_results[0]}，麵包:{temp_results[1]}，煮麵:{temp_results[2]}，雅：{temp_results[3]}，\
        包餐：{temp_results[4]}，點餐：{temp_results[5]}，飲料：{temp_results[6]}，機動：{temp_results[7]}")
        print(f"####")
        print(f" ")

    
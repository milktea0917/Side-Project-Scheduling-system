from reporter import CreatingXlsx

def check_absent(date, worker_list):

    absent_pick = []

    for i in range(len(worker_list)):

        if date in worker_list[i].absent_time:
            print(f"## {worker_list[i].name}今天請假. ##\n")
            absent_pick.append(i)

    return absent_pick

def ArrangeAlgo(work_space, worker_list, date):

    """
    ToDo: 
        1. if weekday split to two part of arranging
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
    already_pick = [0] * len(worker_list)

    if work_space == 4: # if weekday

        # Xaio li 0600~0930 (No Thu)
        # Lan 1000~1400 (Mon.~ Fri.)
        absent_pick = check_absent(str(date), worker_list)
        for i in [0,1,2,7]: 
            candidate_index = -9999
            current_max = -9999

            for j in range(len(worker_list)):
                if (already_pick[j] != 0) or ( j in absent_pick): # one person for one workspace
                    continue
                if (current_max < worker_list[j].ability_list[i]):
                    current_max = worker_list[j].ability_list[i]
                    candidate_index = j

            arranging_list.append(worker_list[candidate_index].name)
            already_pick[candidate_index] = 1

    else: # if weekday

        absent_pick = check_absent(str(date), worker_list)
        for i in range(work_space): 
            candidate_index = -9999
            current_max = -9999

            for j in range(len(worker_list)):
                if (already_pick[j] != 0) or ( j in absent_pick): # one person for one workspace
                    continue
                if (current_max < worker_list[j].ability_list[i]):
                    current_max = worker_list[j].ability_list[i]
                    candidate_index = j

            arranging_list.append(worker_list[candidate_index].name)
            already_pick[candidate_index] = 1

    return arranging_list, already_pick

def Arranging(ReportXlsx, work_space, worker_list, date, week, month):

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
    arranging_list, already_pick = ArrangeAlgo(work_space, worker_list, date)
    

    # ReportXlsx.WriteDF(arranging_list, already_pick, date, week, week_count, month) # ToDo
    ReportXlsx.DFtoTXT(arranging_list, date, week, month)
    # ReportXlsx.ShowDailyResult(work_space, arranging_list)

    return arranging_list, already_pick

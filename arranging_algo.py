def arranging_version1(work_space, worker_list):

    """
    version explaination:
        1. This version is for greedy selection.

    ToDo:
        1. Constrains by the ability score from given.  
        2. Let extra favor added. eg. Lan + May is wellcome to appear together.
    """
    
    """
    variable explaination:
        1. arranging_list: final return
        2. work_space: how many jobs is there in the kitchen
        3. worker_list: list with employee(class)
    """

    arranging_list = []
    for i in range(work_space):
        candidate_index = 0
        current_max = 0
        for j in range(len(worker_list)):
            if current_max < worker_list[j].ability_list[i]:
                current_max = worker_list[j].ability_list[i]
                candidate_index = j
            else:
                continue
        arranging_list.append(worker_list[candidate_index].name)

    return arranging_list
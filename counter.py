def merging_arranging_results(wker_list, wker_ct , arranging_dictionary):
        assert len(wker_list) == len(wker_ct)
        for i in range(len(wker_list)):
            temp_name = wker_list[i].name
            arranging_dictionary[temp_name] = arranging_dictionary[temp_name] + wker_ct[i]
        
        return arranging_dictionary
    
def printing_results(worker_list, arranging_dictionary):
    
    for i in range(len(worker_list)):
        print(f"{worker_list[i].name} 這個月上班 {arranging_dictionary[worker_list[i].name]} 天。")

def showing_arranging_results(worker_list, weekday_worker_list, weekend_worker_list, weekday_counter, weekend_counter):
    
    arranging_dictionary = {}
    for i in range(len(worker_list)):
        arranging_dictionary[worker_list[i].name] = 0

    arranging_dictionary = merging_arranging_results(weekday_worker_list, weekday_counter, arranging_dictionary)
    arranging_dictionary = merging_arranging_results(weekend_worker_list, weekend_counter, arranging_dictionary)
    printing_results(worker_list, arranging_dictionary)
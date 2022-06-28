def sequencial_search_count(list,item):
    count=0
    for i in range(len(list)):
        count= count+1
        if list[i] == item:
            return count
        
    return count


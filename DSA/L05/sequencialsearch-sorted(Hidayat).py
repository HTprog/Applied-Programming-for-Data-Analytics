def ordered_sequencial_search_count(list,item):
    count=0
    for i in range(len(list)):
        count= count+1
        if list[i] > item:
            print('item not found')
            return print('Number of iterations= ',count)
            
        elif list[i]==item:
            print('item found')
            return print('Number of iterations= ',count)

    print('Item not found')
    return print('Number of Iterations=',count)
            

itemlist=[1,2,4,5,6,7]

ordered_sequencial_search_count(itemlist,3)
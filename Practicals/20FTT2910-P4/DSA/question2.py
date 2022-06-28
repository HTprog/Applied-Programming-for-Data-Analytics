#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS
def ordered_sequencial_search(list,item):
    count=0
    for i in range(len(list)):
        count= count+1
        if list[i] > item:
            print('{} not found in the list after {} iterations'.format(item,count))
            return 
            
        elif list[i]==item:
            print('{} is found after {} iterations'.format(item,count))
            return 

    print('{} not found in the list after {} iterations'.format(item,count))
    return 

TestList=[1,2,3,4,5,7]
ordered_sequencial_search(TestList,3)
ordered_sequencial_search(TestList,6)
            
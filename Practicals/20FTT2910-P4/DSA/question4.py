#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS
def RangeSearch(list,a,b):
    results=[]
    for i in range(len(list)):
        if list[i] in range(a,b):
            results.append(list[i])
        else:
            continue
    if len(results)==0:
        print('Range Search Result:{}'.format('No result found'))
        return
    else:
        print('Range Search Result:',end='')
        print(results)
    return
List=[0, 1, 2, 8, 13, 17, 19, 32, 42]

RangeSearch(List,2,12)
RangeSearch(List,20,25)
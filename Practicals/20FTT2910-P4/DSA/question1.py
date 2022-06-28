#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS
def sequentialSearch(alist, item):
    pos = 0
    while pos < len(alist):
        if alist[pos] == item:
            print('{} found at position {}'.format(item,pos))
            return
        else:
            pos = pos+1
    print('{} is not found in the list'.format(item))
    return
    


TestList=[4,5,3,2,1]

sequentialSearch(TestList,3)
sequentialSearch(TestList,6)
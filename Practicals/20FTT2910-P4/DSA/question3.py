#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            print('{} was found at {}'.format(item,midpoint))
            return

        elif item < a_list[midpoint]:
                last = midpoint - 1 
        else:
            first = midpoint + 1
    print('{} was not found'.format(item))
    return 

List=[0, 1, 2, 8, 13, 17, 19, 32, 42] 
binary_search(List,37)
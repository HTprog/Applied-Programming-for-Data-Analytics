def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        print('Iterations')
        print('first=',first)
        print('last=',last)
        print('mid=',midpoint)
        #first condition - if item is equal to midpoint
        if a_list[midpoint] == item:
            found = True

        #second condition - items is less than midpoint -> reassign last value
        elif item < a_list[midpoint]:
                last = midpoint - 1 #4-1
                #new las = 3, my first is still 0
        else:
            first = midpoint + 1
            #first -> 1
            #last -> 3
    return found

# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]#9 items
# print(binary_search(test_list, 3))
# print(binary_search(test_list, 13))

act5=[3, 5, 6, 8, 11, 12, 14, 15, 17, 18] #Ans= pos (4,1,2,3) / (11,5,6,8)
print(binary_search(act5, 8))

def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

def linear_search(list, item):
    for i in range(len(list)):
    #for i in list:
        if item == list[i]:
            return True
    return False

print(linear_search(testlist,3))
print(linear_search(testlist,13))

itemlist=[1,2,4,5,6,7]
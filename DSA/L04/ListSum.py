def list_sum(num_list):
    the_sum = 0

    for i in num_list:
        the_sum = the_sum + i
        print(the_sum , " + " , i)
    return the_sum

print(list_sum([1,2,3,5,7,9]))

#recursive

def list_sum_recursive(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        #print(num_list[0] , " + " , list_sum_recursive(num_list[1:]))
        return num_list[0] + list_sum_recursive(num_list[1:])

print(list_sum_recursive([1,2,3,5,7,9]))

def list_sum_recursive2(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        a= num_list[0]
        b = list_sum_recursive2(num_list[1:])
        print (a , " + " , b)
        return a+b

print(list_sum_recursive2([1,2,3,5,7,9]))

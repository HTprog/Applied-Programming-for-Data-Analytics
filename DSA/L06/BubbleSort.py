def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1): #9 passes
        print('pass no', pass_num)
        for i in range(pass_num): 
            if a_list[i] > a_list[i + 1]:
                print('Exchange', a_list[i], 'with', a_list[i+1])
                temp = a_list[i]
                #temp - to temporarily store the original variable
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
            else:
                print('No exchange')
                

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)

#short bubble sort

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

a_list=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(a_list)
print(a_list)
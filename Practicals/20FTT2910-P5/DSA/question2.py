#Muhammad Hidayat Hidayat Bin Mohd Yusof
#20FFTT2910
#DA3306 DATA STRUCTURES AND ALGORITHMS
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1): 
        print('pass no', pass_num)
        for i in range(pass_num): 
            if a_list[i] > a_list[i + 1]:
                print('Exchange', a_list[i], 'with', a_list[i+1])
                temp = a_list[i]
                
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
            else:
                print('No exchange')
    print('sorting complete\n')
    print('Sorted list:',List)
                

List = [54, 93, 17, 20]
bubble_sort(List)


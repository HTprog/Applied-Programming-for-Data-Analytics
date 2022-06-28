# Muhammad Hidayat Hidayat Bin Mohd Yusof
# 20FFTT2910
# DA3306 DATA STRUCTURES AND ALGORITHMS
def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid1 = int(len(a_list) * 1/3)
        mid2 = int(len(a_list) * 2/3)
        left_half = a_list[:mid1]
        mid_half = a_list[mid1:mid2]
        right_half = a_list[mid2:]
        merge_sort(left_half)
        merge_sort(mid_half)
        merge_sort(right_half)

        i = 0
        j = 0
        l = 0
        k = 0

        while i < len(left_half) and j < len(right_half) and l < len(mid_half):
            if left_half[i] < right_half[j]:
                if left_half[i]<mid_half[l]:
                    a_list[k] = left_half[i]
                    i = i + 1
                else:
                    a_list[k] = mid_half[l]
                    l = l + 1
            
            elif mid_half[l]<right_half[j]:
                if 
            # else:
            #     a_list[k] = right_half[j]
            #     j = j + 1
                
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

        print("Merging ", a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
# print(a_list)

# mid1 = int(len(a_list) * 1/3)
# mid2 = int(len(a_list) * 2/3)
# print(mid1)
# print(mid2)

# left_half = a_list[:mid1]
# mid_half = a_list[mid1:mid2]
# right_half = a_list[mid2:]

# print(left_half)
# print(mid_half)
# print(right_half)
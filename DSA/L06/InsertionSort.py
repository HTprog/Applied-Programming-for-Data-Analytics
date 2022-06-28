def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        # print("Current value", current_value)
        # print("position", position)
        print('pass no', index)
        print(a_list)

        while position > 0 and a_list[position - 1] > current_value:
            # print('Exchange', a_list[position], 'with', a_list[position - 1])
            a_list[position] = a_list[position - 1]
            # print('position', position)
            position = position - 1 
            a_list[position] = current_value


a_list = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
insertion_sort(a_list)
print(a_list)


#삽입정렬

def insertion_sort(my_list):
    for i in range(len(some_list)):
        key = some_list[i]
        j = i - 1
        while j >= 0 and some_list[j] > key :
            some_list[j+1] = some_list[j]
            j = j-1
        some_list[j+1] = key


some_list = [11,3,6,4,12,1,2]
insertion_sort(some_list)
print(some_list)

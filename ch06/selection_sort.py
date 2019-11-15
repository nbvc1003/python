

def selecttion_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] > my_list[j]:
                # 두변수를 바꿔준다. !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                my_list[j], my_list[i] = my_list[i], my_list[j]
    return my_list


print(selecttion_sort([2,3,4,1,6,7]))



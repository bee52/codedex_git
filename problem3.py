problem = "problem3"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

import random
"""
source of bubble sort, selection sort and mrge sort code:
@author: ericgrimson
"""
bubble_num_comparisons = 0
#bubble sort
def bubble_sort(L):
    global bubble_num_comparisons
    bubble_num_comparisons = 0

    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            bubble_num_comparisons += 1
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

selection_num_comparisons = 0                
# selection sort
def selection_sort(L):
    global selection_num_comparisons
    selection_num_comparisons = 0

    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            selection_num_comparisons += 1
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

#merge sort
merge_num_comparisons = 0
def merge(left, right):
    global merge_num_comparisons
    merge_num_comparisons = 0
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        merge_num_comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while (i < len(left)):
        merge_num_comparisons += 1
        result.append(left[i])
        i += 1
    while (j < len(right)):
        merge_num_comparisons += 1
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result
       
def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
        
        
def sort_comparison(list_size, sorted = False):
    # code here
    my_list = random.sample(range(1, 101), list_size)
    print("List of size", list_size, " to sort is ", my_list)
    if sorted == False:
        bubble_sort(my_list)
        print("number of comparisons for bubble sort : ", bubble_num_comparisons)

        selection_sort(my_list)
        print("number of comparisons for selection sort : ", selection_num_comparisons)

        merge_sort(my_list)
        print("number of comparisons for merge sort : ", merge_num_comparisons)

    if sorted == True:
        #sort the list using bubble sort first
        print("sorting the list...")
        sorted_list = bubble_sort(my_list)
        print("The sorted list : ", sorted_list)
        #compare number of comparisions on the sorted list
        bubble_sort(sorted_list)
        print("number of comparisons for bubble sort : ", bubble_num_comparisons)

        selection_sort(sorted_list)
        print("number of comparisons for selection sort : ", selection_num_comparisons)

        merge_sort(sorted_list)
        print("number of comparisons for merge sort : ", merge_num_comparisons)



    #print('sort_comparison not implemented')

sort_comparison(7, True)
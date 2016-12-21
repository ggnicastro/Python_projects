"""Merge and sort algorithm"""

def MergeSort(lst):
    print "Splitting list ", lst
    #base case
    if len(lst) <=1:
        print "len = 1", lst
        return lst
    if len(lst) > 1:
        mid_lst = len(lst)//2
        left_lst = lst[:mid_lst]
        right_lst = lst[mid_lst:]
        #Recursive call
        MergeSort(left_lst)
        MergeSort(right_lst)
        print left_lst
        print right_lst
        #Merge
        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i +=1

            else:
                lst[k] = right_lst[j]
                j +=1

            k +=1
        while i < len(left_lst):
            lst[k] =left_lst[i]
            i +=1
            k +=1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j+=1
            k+=1
        print "Merging", lst
        return lst

lst_odd = [100,75,37,29,18]
lst_even = [10,8,2,1,3,4]

MergeSort(lst_odd)
MergeSort(lst_even)
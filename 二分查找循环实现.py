def binary_search_2(alist,item):
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] ==item:
            return True
        elif item < alist[mid]:
            last = mid - 1  #向左移
        else:
            first = mid + 1   #向右移
    return False
if __name__ == "__main__":
    a = [1,5,6,10,11,13,18,37,99]
    sorted_list_21 = binary_search_2(a, 18)
    print(sorted_list_21)    #True
    sorted_list_22 = binary_search_2(a, 77)
    print(sorted_list_22)    #False
def binary_search(alist,item):
   # """二分查找---递归实现"""
    n = len(alist)
    if n > 0:
        mid = n//2    #数组长度的一半中间下标
        if item == alist[mid] :
            return True   #查找成功
        elif item < alist[mid]:
            return binary_search(alist[:mid],item) #查找目标在列表的左半快
        else:
            return binary_search(alist[mid+1:], item)
    else :
        return False   #失败
if __name__ == "__main__":
    a = [1,5,6,10,11,13,18,37,99]
    # print(a)
    sorted_list_11 = binary_search(a,37)
    print(sorted_list_11)   #True
    sorted_list_12= binary_search(a, 88)
    print(sorted_list_12)   #False
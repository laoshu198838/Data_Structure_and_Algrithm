# coding='utf-8'
def quick_sort(alist, first, last):
    # 递归的退出条件
    if first >= last:
        return
    
    high = last
    low = first
    mid_value = alist[first]
    
    while low < high:
        # 让high的游标左移动
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        
        # 让low往右边移动
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1删掉了以免high和low错过
        # 从循环当中退出
    
    # 对low左边的列表进行排序
    alist[low] = mid_value
    
    # 对low右边的列表进行排序
    quick_sort(alist,0,low-1)
    
    # 切片返回性的列表
    quick_sort(alist, low + 1, last)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)
    
  
    
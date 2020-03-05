# coding='utf-8'


def binarysearch(alist, item):
    """ 二分查找，递归版 """
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binarysearch(alist[mid+1:], item)
        else:
            return binarysearch(alist[:mid], item)
    return False


def binarysearch_2(alist, item):
    """ 二分查找，非递归 ,alist必须是有序的，必须是列表，有序列号"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item > alist[mid]:
            first = mid+1
            last = n-1
        else:
            first = 0
            last = mid
    return False


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(li)
    print(binarysearch(li, 55))
    print(binarysearch(li, 100))

    print(binarysearch_2(li, 17))
    print(binarysearch_2(li, 100))

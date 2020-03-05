# coding:utf-8

def insertsort(alist):
    n=len(alist)
    for i in range(1,n):
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i += -1
            else:
                break
    return alist


if __name__ == "__main__":
    li = [100, 16, 17,15,121,11,26,27]
    print(li)
    insertsort(li)
    print(li)            

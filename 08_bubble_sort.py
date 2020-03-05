# coding:utf-8


def bubble_sort(alist):
    n=len(alist)
    for j in range(n-1,1,-1):
        count=0#算法优化代码，如果循环一次没有发生交换说明顺序已经排好，直接返回。
        for i in range(j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
        if count==0:
            return
    return alist

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

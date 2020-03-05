# coding=utf-8
def shellsort(alist):
    n=len(alist)
    gap=n//2
    while gap >= 1:
        # 希尔排序与插入排序的区别，至于gap怎么取，就是数学问题，数学取得好就能够取得最优算法
        for i in range(gap, n):
            while i > 0:
            # 每一行进行插入
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i += -gap
                    # 插入法的移动
                else:
                    break
                    # 优化算法，当比前面大了之后就可以退出了
        gap //= 2
        # gap每次缩小一倍

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shellsort(li)
    print(li)
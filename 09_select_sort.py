# coding:utf-8

def select_sort(alist):
    n=len(alist)
    for j in range(n-1,0,-1):#1-n-1
        max_index=j#指针用于记录最大值的位置
        for i in range(j):#0-j-1
            if isinstance(alist[i],list) or isinstance(alist[i],tuple):#判断i索引号的元素是否为列表或元组,此处用is进行判断会报错
                if isinstance(alist[max_index],tuple) or isinstance(alist[max_index],list):#判断指针元素是否为元组和列表
                    if alist[max_index][0]<alist[i][0]:#列表与单个元素比较
                        max_index=i
                    else:
                        if alist[max_index][0]==alist[i][0] and alist[max_index][1]<alist[i][1]:#列表与列表中元素比较
                            max_index=i
                else:
                    if alist[max_index]<=alist[i][0]:#列表与单个元素比较
                        max_index=i
            else:#i索引号的元素不为列表或元组
                if isinstance(alist[max_index],tuple) or isinstance(alist[max_index],list):#判断指针元素是否为元组和列表
                    if alist[max_index][0]<alist[i]:
                        max_index=i
                else:
                    if alist[max_index] < alist[i]:#比较对象都为数值
                         max_index=i
        alist[max_index],alist[j]=alist[j],alist[max_index]

if __name__ == "__main__":
    li = [100, [16, 1], [16, 2], 15, 121, 11, 26, 27]
    print(type(li[0]))
    print(li)
    select_sort(li)
    print(li)
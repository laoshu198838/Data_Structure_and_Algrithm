class Node(object):
    """结点"""
    def __init__(self, item):
        self.elem=item
        self.pre=None
        self.next=None

class DoublecircleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head=node
    
    def is_empty(self):
        """链表是否为空"""
        return self.__head==None
    
    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        count=0
        cur=self.__head
        # count记录数量
        if self.is_empty():
            return 0
        else:
            if cur.next == cur:
                return 1
            else:
                while cur.next != self.__head:
                    cur=cur.next
                    count+=1
                return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        if self.is_empty():
            print('False:list is empty')
            return
        else:
            if cur.next == cur:
                print(cur.elem)
                return
            else:
                while cur.next != self.__head:
                    print(cur.elem,end=' ')
                    cur=cur.next
                print(' ')

    def add(self, item):
        """链表头部添加元素，头插法"""
        node=Node(item)
        if self.is_empty():#list为空时，cur.next不存在
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next=self.__head
            self.__head=node
            node.next.pre = node
            cur.next = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        
        #区分空链表和非空链表进行讨论
        if self.is_empty():#判断链表是否为空链表
            self.__head = node
            node.next = node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            cur.next=node
            node.pre = cur
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            count=0
            node=Node(item)
            cur=self.__head
            while count!=pos:
                count+=1
                cur=cur.next
            #先对新加入的节点进行绑定，然后再修改以前绑定的节点
            node.next=cur
            node.pre=cur.pre
            cur.pre.next=node
            cur.pre=node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        if self.is_empty():
            return False
        else:
            if self.length() == 1:
            #因为是循环链，所以当length为1时，cur.next==self.__head,需要单独考虑
                if cur.elem == item:
                    self.__head = None
                    return True
                else:
                    return False
            else:
                while cur.next != self.__head:
                    if cur.elem==item:
                        if cur==self.__head:#判断是否是头结点
                            self.__head=cur.next
                            if cur.next:# 判断链表是否只有一个结点
                                cur.next.pre=None
                        else:#对不是头结点的情况进行分析
                            cur.pre.next=cur.next
                            if cur.next:
                                cur.next.pre=cur.pre
                        break
                    else:#没有找到item的时候进行循环
                        cur=cur.next
    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        count = 0
        if self.is_empty():
            print("list is empty")
            return 
        else:
            while cur.next != self.__head:
                cur = cur.next
                count += 1
            print(item+'的NO：'+count)
            print(item+'的ID：'+id(cur))

if __name__ == "__main__":
    ll = DoublecircleLinkList()
    ll.travel()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    ll.travel()
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.travel()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
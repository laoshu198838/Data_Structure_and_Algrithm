# coding:utf-8


class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    
    def travel(self): """遍历整个链表"""
        cur = self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print('')

    def add(self, item):
        """链表头部添加元素，头插法"""
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node=Node(item)#先使用这个元素创建一个节点，
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
            node.next=pre.next
            pre.next=node

    def remove(self, item):
        """删除节点"""
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.elem==item:
                if cur==self.__head:
                    self.__head=cur.next
                else:
                     pre.next=cur.next
                break
            pre=cur
            cur=cur.next
    
    def search(self, item):
        """查找节点是否存在"""
        cur=self.__head count=0
        while cur!=None: if cur.elem==item: print('True')
                return True count+=1
            cur=cur.next
            return False
if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.append(10)
    print(sll.length())
    sll.travel()
    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.travel()
    sll.remove(10)
    sll.travel()
    print(sll.search(8))
    sll.insert(0,110)
    sll.travel()
    sll.insert(100,120)
    sll.travel()
    print(id(110))
    print(id(8))
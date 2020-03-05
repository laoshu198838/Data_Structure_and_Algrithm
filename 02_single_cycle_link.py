# coding:utf-8


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
           

class SingleLinkcircleList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node     

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None
        
    def length(self): """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 1
        if self.is_empty():
            return 0
        else:
            while cur.next != self.__head:
                cur = cur.next
                count += 1
            return count      

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        if self.is_empty():
            return
        else:
            if self.length == 1:
                print(cur.elem)
            else:
                while cur.next != self.__head:
                    print(cur.elem,end=' ')
                    cur = cur.next
                print(cur.elem)   
    
    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            cur = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node
        
    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
      
    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        node = Node(item)
        cur = self.__head
        pre = None
        count = 1
        if pos <= 0:
            self.add(item)
            print(True)
            return
        else:
            if pos > self.length():
                self.append(item)
            else:
                while count < pos:
                    cur = cur.next
                    pre = cur
                pre.next = node
                node.next = cur
        
    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        if self.is_empty():
            print(False)
            return False
        else:
            if self.length == 1:
                if cur.elem == item:
                    cur = None
            else:
                while cur.next != self.__head:
                    if cur.elem == item:
                        if cur == self.__head:   
                            self.__head = cur.next
                        else:
                            pre.next = cur.next
                        break
                    pre = cur
                    cur = cur.next
           
    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        count = 0
        if self.length == 1:
            if cur.elem == item:
                return True
            else:
                return False
        else:
            while cur.next != self.__head:
                if cur.elem==item:
                    return True
                count+=1
                cur=cur.next
            return False

if __name__=='__main__':
    sll=SingleLinkcircleList()
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
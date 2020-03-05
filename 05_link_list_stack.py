# coding:utf-8 class Node(object): def __init__(self,item): self.elem=item self.next=None
class Stack(object):
    """栈"""
    def __init__(self,node=None):
        self.__head=node

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        node = Node(item)
        if self.__head==None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def pop(self):
        """弹出栈顶元素"""
        pre=None
        cur=self.__head
        while cur.next!=None:
            pre=cur
            cur=cur.next
        pre = None
        
    def peek(self):
        """返回栈顶元素"""
        cur=self.__head
        while cur.next!=None:
            cur=cur.next
        return cur.elem

    def is_empty(self):
        """判断栈是否为空"""
        return self.__head==None
        # return not self.__list

    def size(self):
        """返回栈的元素个数"""
        count=0
        cur=self.__head
        while cur!=None:
            cur=cur.next
            count+=1
        return count
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    s.push(100)
    print(s.peek())
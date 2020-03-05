# coding:utf-8
#栈的特点是后进先出，可以用链表，列表、顺序表实现

class Stack(object):
    """栈"""
    def __init__(self):
        self.__list_1=[]#此处的list_1同理可以用其他的替代不过一般是用list代替，本人用list_1主要是为了检验它是否可以用其他的替代。

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list_1.append(item)#此处是在尾部添加，同理在头部也可以添加。

    def pop(self):
        """弹出栈顶元素"""
        return self.__list_1.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list_1:
            return self.__list_1[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return len(self.__list_1)==0
        # return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list_1)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.size())
    print(s.is_empty())
    print(s.peek())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
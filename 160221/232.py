class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        tempList = []
        length = len(self.list)
        for i in range(0, length - 1):
            tempList.append(self.list.pop())
        self.list.pop()
        for i in range(0, length - 1):
            self.list.append(tempList.pop())
        return

    def peek(self):
        """
        :rtype: int
        """
        tempList = []
        length = len(self.list)
        for i in range(0, length):
            tempList.append(self.list.pop())
            
        result = tempList.pop()
        self.list.append(result)
        for i in range(0, length - 1):
            self.list.append(tempList.pop())
        

        return result

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0
        
def test():
    q = Queue()
    q.push(1)
    print q.peek()
    q.push(2)
    q.pop()
    print q.peek()
test()
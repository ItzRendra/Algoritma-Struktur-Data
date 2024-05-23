class Node():
    def __init__(self, data):
        self.data = data
        self.pointer = None

kosong = [] 

class LinkedList:
    def __init__(self):
        self.head = None
        
    def printInfo(self):
        
        printval = self.head
        while printval:
            print(printval.data, end=" ")
            kosong.append(printval.data)
            printval = printval.pointer
            
    def atBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.pointer = self.head
        self.head = NewNode
        
    def atEnd(self, newdata):
        NewNode = Node(newdata)
        point = self.head
        while(point.pointer != None):
            point = point.pointer
        point.pointer = NewNode
        
    def atAfter(self, point, newdata):
        NewNode = Node(newdata)
        NewNode.pointer = point.pointer
        point.pointer = NewNode

my = LinkedList()
my.atBeginning(5)
my.atBeginning(4)
my.atBeginning(2)
my.atBeginning(0)


def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    result = []
    for num in nums:
        count = sorted_nums.index(num)
        result.append(count)
    return result

num = [1,1,4,2,1,3]
smallerNumbersThanCurrent(num)
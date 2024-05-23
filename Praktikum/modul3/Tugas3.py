# linked list
class Node(object):
    """This is a node object"""
    def __init__(self, data=None):
        # Inisialisasi node dengan data dan pointer ke None
        self.data = data
        self.pointer = None

class LinkList(object):
    def __init__(self, head):
        # Mendefinisikan head dari linked list baru
        self.head = head

    def PrintLinkedList(self):
        # Mencetak semua anggota dari linked list
        printval = self.head
        line = []
        while printval is not None:
            line.append(printval.data)
            printval = printval.pointer
        print(line)

    def getDataPosition(self, data):
        # Mengembalikan posisi node dengan data yang diberikan
        position = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return position
            current_node = current_node.pointer
            position += 1
        return -1  # Data tidak ditemukan dalam linked list

    def AtBegining(self, newdata):
        # Menyisipkan node baru di awal linked list
        NewNode = Node(newdata)
        NewNode.pointer = self.head
        self.head = NewNode

    def AtEnd(self, newdata):
        # Menyisipkan node baru di akhir linked list
        NewNode = Node(newdata)
        laste = self.head
        while(laste.pointer != None):
            laste = laste.pointer
        laste.pointer = NewNode

    def Inbetween(self, middle_node, newdata):
        # Menyisipkan node baru di tengah linked list
        NewNode = Node(newdata)
        NewNode.pointer = middle_node.pointer
        middle_node.pointer = NewNode

    def RemoveNode(self, Removekey):
        # Menghapus node dari linked list
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.pointer
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.pointer

        if (HeadVal == None):
            return

        prev.pointer = HeadVal.pointer
        HeadVal = None
    
# make initial Nodes & their pointers
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)
a.pointer = b
b.pointer = c
c.pointer = d

linlis = LinkList(a) #create a new linlist
linlis.PrintLinkedList() #print the linlist traversing
print("===========================")
linlis.AtBegining(3) #insert at beginning
linlis.PrintLinkedList()
print("===========================")
linlis.AtEnd(7) #insert at end of list
linlis.PrintLinkedList()
print("===========================")
linlis.Inbetween(b,50) # insert Node after b node
linlis.PrintLinkedList()
print("===========================")
linlis.RemoveNode(50) # remove node with data 50
linlis.PrintLinkedList() # 3+5+2+6+9+7
print("==========================")
# linlis.searchData(6)
print(linlis.getDataPosition(6))

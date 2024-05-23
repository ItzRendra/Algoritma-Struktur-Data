class Node(object):
    def __init__(self, data=None):
        # Inisialisasi node dengan data, next pointer, dan prev pointer
        self.data = data
        self.next = None
        self.prev = None

class doblyLinkList(object):
    def __init__(self, head, tail):
        # Mendefinisikan head dan tail dari linked list baru
        self.head = head
        self.tail = tail

    def PrintNext(self):
        # Mencetak semua anggota dari linked list secara forward
        printval = self.head
        line = []
        while printval is not None:
            line.append(printval.data)
            printval = printval.next
        print(line)

    def PrintPrev(self):
        # Mencetak semua anggota dari linked list secara backward
        printval = self.tail
        line = []
        while printval is not None:
            line.append(printval.data)
            printval = printval.prev
        print(line)

    def insertAtBegining(self, newdata):
        # Menyisipkan node baru di awal linked list
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head.prev = NewNode
        self.head = NewNode

    def insertAtEnd(self, newdata):
        # Menyisipkan node baru di akhir linked list
        NewNode = Node(newdata)
        NewNode.prev = self.tail
        self.tail.next = NewNode
        self.tail = NewNode


# make initial Nodes & their pointers
a = Node(5)
b = Node(2)
c = Node(6)
d = Node(9)

b.prev = a
a.next = c.prev = b
b.next = d.prev = c
c.next = d

doblylis = doblyLinkList(a , d) # init new doblyLinkList
doblylis.PrintNext()
doblylis.PrintPrev()
print("=====================")
doblylis.insertAtBegining(50)
doblylis.PrintNext()
doblylis.PrintPrev()
print("=====================")
doblylis.insertAtEnd(70)
doblylis.PrintNext()
doblylis.PrintPrev()

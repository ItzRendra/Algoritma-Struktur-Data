class bank:
    def __init__(self, nama, nomor, saldo):
        self.nama = nama
        self.nomor = nomor
        self.saldo = saldo
        
    def cekSaldo(self):
        print("Saldo : ", self.saldo)

    def cekNama(self):
        print("Nama : ", self.nama)

    def cekNomor(self):
        print("Nomor Rekening : ", self.nomor)
    
    def tambahSaldo(self, tambah):
        self.saldo = self.saldo + tambah
        print('Jumlah Setoran : ', tambah, '\nSaldo Akhir : ', self.saldo)
    
    def tarikSaldo(self, kurang):
        self.saldo = self.saldo - kurang
        print('Uang yang di tarik : ', kurang, '\nSaldo Akhir : ', self.saldo)
    
# org = bank("Raka", 1111, 50000)
# 
# org.cekNama()
# org.cekSaldo()
# org.cekNomor()
# org.tambahSaldo(10000)
# org.tarikSaldo(30000)

# no2
"""
>Kemutabilan (Mutability)

List bersifat mutable, yang berarti isinya dapat diubah setelah pembuatan. Anda dapat menambah, menghapus, atau mengubah elemen dalam list.
Tuple bersifat immutable, yang berarti isinya tidak dapat diubah setelah pembuatan. Anda tidak dapat menambah, menghapus, atau mengubah elemen dalam tuple secara langsung.


>Sintaksis

List ditulis dengan menggunakan tanda kurung siku [ ], misalnya list = [1, 2, 3].
Tuple ditulis dengan menggunakan tanda kurung biasa ( ), misalnya tuple = (1, 2, 3).


>Penggunaan

List lebih cocok digunakan ketika Anda membutuhkan kumpulan nilai yang dapat diubah, seperti dalam kasus di mana Anda perlu menambah atau menghapus elemen.
Tuple lebih cocok digunakan ketika Anda membutuhkan kumpulan nilai yang tidak dapat diubah, seperti dalam kasus di mana Anda ingin memastikan integritas data atau menjamin bahwa nilai tidak akan berubah.


>Performa

Secara umum, tuple sedikit lebih cepat daripada list dalam hal pemrosesan karena tuple bersifat immutable dan lebih sederhana dalam implementasinya.


>Jumlah Elemen

List dapat memiliki jumlah elemen yang berubah-ubah selama runtime.
Tuple memiliki jumlah elemen yang tetap setelah pembuatan."""



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
x
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.append(3)
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.insert_after(linked_list.head.next, 4)
linked_list.print_list()  # Output: 1 2 4 3

linked_list.delete_node(4)
linked_list.print_list()  # Output: 1 2 3
    
    
        
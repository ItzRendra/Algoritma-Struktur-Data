#@author Raka Rendra Fayanto | L200224246 
def primeOrNot(n): #Fungsi untuk mengecek apakah angka yang di masukan adalah bilangan prima atau tidak
    if n > 1: #bilangan prima adalah bilangan bilangan yang lebih dari satu dan tidak memiliki faktor selain 1 dan bilangan terserbut
        for i in range(2, (n//2)+1): #membuat range untuk mengecek apakah bilangan adalah bilangan prima atau tidak
            if n % i == 0: #bilangan prima tidak bisa di bagi bilangan tersebut dan satu,
                        #jika sisa bagi suatu bilangan = 0 maka bilangan tersebut adalah bilangan prima
                print (n, "adalah bukan bilangan prima")
                print ("NIM = L200224246")
                break
            else:
                print(n, "adalah bilangan prima")
                print ("NIM = L200224246")
                break
    else: #handling jika user memberikan inputan angka kurang dari 1 dan kurang dari satu
        print(n, "bukanlah bilangan prima atau kurang sama dengan satu, tolong masukan angka lebih dari satu!")
        print ("NIM = L200224246")

#===================================================================================#
#===================================================================================#
A = [2,2,3,4,4,4,5,5,6,7]
def delMultipleList(A): #fungsi untuk menghilangkan isi list yang lebih dari satu
    for i in A: #iterasi untuk mengecek setiap isi
        if A.count(i) > 1: #mengecek isi list apakah ada yang lebih dari satu
            A.remove(i) # jika terdapat pengulangan atau isi list lebih dari satu maka menghapus element yang di cek saat ini
    print("New List =", A)
    print ("NIM = L200224246")

#===================================================================================#
#===================================================================================#

def sumNum(n): #fungsi untuk menjumlahkan bilangan n dengan bilangan sebelumnya
    z = 0 #variable wadah untuk penjumlahan
    if n > 0: # mengecek apakah input user lebih dari 0 agar dapat di proses
        for i in range(1, n+1): # pengulangan n kali untuk menjumlahkan angka sebelum n
            z = z + i # menambahkan setiap angka sebelumnya dengan iterasi dari for loop jika masih belum sampai n batas
        print ("jumlah bilangan", "dari 1 sampai", n , "adalah : ", z) #mencetak hasil akhir
        print ("NIM = L200224246")
    else: #jika angka n/input kurang dari 0
        for i in range(1, n-1, -1): # pengulangan ke angka negatif dengan *step* mundur
            z = z + i #penambahan pada bilangan sebelumnya jika input adalah angka negatif
        print ("jumlah bilangan", "dari 1 sampai ",n , " adalah : ", z) #mencetak hasil akhir
        print ("NIM = L200224246")
#===================================================================================#
#===================================================================================#

        

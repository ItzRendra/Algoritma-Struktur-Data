# matriks nol

def matrixZero(n ,m = None) : # n = jumlah baris , m= jumlah kolom
  if m is None : m = n # jika jumlah kolom tidak ada, maka dianggap, n = m
  return [[0 for j in range(m)] for i in range(n)] # Membuat matrix nol dengan hasil ukuran

# matrix identitas

def identityMatrix(n) :
  result = [[0 for j in range(n)] for i in range(n)] # Membuat matrix nol dengan hasil ukuran
  for i in range(n) :
    result[i][i] = 1
  return result

print(matrixZero(5,4))
print(identityMatrix(5))
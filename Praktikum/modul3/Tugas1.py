def consistent(matrik):
    # Memeriksa apakah setiap baris pada matriks memiliki panjang yang sama dengan baris pertama
    for i in matrik:
        if len(i) != len(matrik[1]):
            return False
    return True

def getMatrixSize(matrik):
    # Jika matriks konsisten, mengembalikan ukuran matriks dalam bentuk tuple (baris, kolom)
    # Jika matriks tidak konsisten, menampilkan pesan "Matrik Tidak Konsisten" dan mengembalikan None
    if consistent(matrik):
        return (len(matrik), len(matrik[0]))
    else:
        print("Matrik Tidak Konsisten")
        return None

def sumMatrix(matrik1, matrik2):
    # Memeriksa apakah kedua matriks konsisten
    if consistent(matrik1) and consistent(matrik2):
        # Mendapatkan ukuran kedua matriks
        size1 = getMatrixSize(matrik1)
        size2 = getMatrixSize(matrik2)
        # Jika ukuran kedua matriks tidak sama, tampilkan pesan "Ukuran matrik harus sama!" dan kembalikan None
        if size1 != size2:
            print("Ukuran matrik harus sama!")
            return None
        # Membuat matriks hasil dengan ukuran yang sama dan diisi dengan 0
        result = [[0 for j in range(size1[1])] for i in range(size1[0])]
        # Menjumlahkan setiap elemen matriks dan menyimpannya ke matriks hasil
        for i in range(size1[1]):
            for j in range(size1[0]):
                result[i][j] = matrik1[i][j] + matrik2[i][j]
        return result
    else:
        print("Ukuran matrik tidak sama!")
        return None

def multiplyMatrices(matrix1, matrix2):
    # Memeriksa apakah kedua matriks konsisten
    if not consistent(matrix1) or not consistent(matrix2):
        print("Ukuran matrik tidak sama!")
        return None
    # Mendapatkan ukuran kedua matriks
    size1 = getMatrixSize(matrix1)
    size2 = getMatrixSize(matrix2)
    # Jika jumlah kolom matriks pertama tidak sama dengan jumlah baris matriks kedua, tampilkan pesan "Ukuran matrix tidak dapat di kalikan" dan kembalikan None
    if size1[1] != size2[0]:
        print("Ukuran matrix tidak dapat di kalikan")
        return None
    # Membuat matriks hasil dengan ukuran yang sesuai
    result = [[0 for j in range(size2[1])] for i in range(size1[0])]
    # Melakukan perkalian matriks
    for i in range(size1[0]):
        for j in range(size2[1]):
            for k in range(size1[1]):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def multiplyMatrices2(matrix1, matrix2):
    # Memeriksa apakah kedua matriks konsisten
    if not consistent(matrix1) or not consistent(matrix2):
        print("salah satu atau kedua matrik tidak memiliku ukuran yang sama!")
        return None
    # Mendapatkan ukuran kedua matriks
    size1 = getMatrixSize(matrix1)
    size2 = getMatrixSize(matrix2)
    # Jika jumlah kolom matriks pertama tidak sama dengan jumlah baris matriks kedua, tampilkan pesan "Ukuran matrik tidak dapat di kalikan" dan kembalikan None
    if size1[1] != size2[0]:
        print("Ukuran matrik tidak dapat di kalikan")
        return None
    # Membuat list kosong untuk menyimpan hasil
    result = []
    # Melakukan perkalian matriks
    for i in range(size1[0]):
        row = []
        for j in range(size2[1]):
            element = 0
            for k in range(size1[1]):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def determinant(matrik):
    # Memeriksa apakah matriks konsisten
    if not consistent(matrik):
        return None
    # Mendapatkan ukuran matriks
    size = getMatrixSize(matrik)
    # Jika matriks tidak bujur sangkar (jumlah baris tidak sama dengan jumlah kolom), kembalikan None
    if size[0] != size[1]:
        return None
    # Jika matriks berukuran 1x1, kembalikan elemen tunggal tersebut
    if size[0] == 1:
        return matrik[0][0]
    # Jika matriks berukuran 2x2, hitung determinannya dengan rumus a*d - b*c
    if size[0] == 2:
        return matrik[0][0] * matrik[1][1] - matrik[0][1] * matrik[1][0]
    # Untuk matriks berukuran lebih besar dari 2x2
    det = 0
    for i in range(size[0]):
        # Membuat submatriks dengan menghilangkan baris ke-i dan kolom ke-j
        submatrix = [row[:i] + row[i+1:] for row in (matrik[:i] + matrik[i+1:])]
        # Menghitung determinan submatriks secara rekursif dan menjumlahkannya dengan operasi pengurangan atau penjumlahan
        det += ((-1) ** i) * matrik[0][i] * determinant(submatrix)
    return det

# testcases
matrik1 = [[1, 2, 3], [1, 1, 2], [2, 1 , 2]]
matrik2 = [[1, 3, 1], [0, 1, 0], [2, 0 , 2]]

# consistency and validation CHECK
if consistent(matrik1) :
  print(matrik1, "konsisten")

# check matrix size
print(getMatrixSize(matrik1))

# add 2 matrices
tambah = sumMatrix(matrik1,matrik2)
print(tambah)
tambah2 = sumMatrix2(matrik1,matrik2)
print(tambah2)

#multiply 2 matrix
print(multiplyMatrices(matrik1,matrik2))
print(multiplyMatrices2(matrik1,matrik2))


# check matrix determinant size 
print(determinant(matrik1))
print(determinant(matrik2))

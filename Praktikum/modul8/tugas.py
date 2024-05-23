import re

# Function untuk mengekstrak kata-kata yang dimulai dengan 'me'
def extract_me_words(file_path):
    try:
        # Buka file dan baca isinya
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Cari semua kata yang diawali dengan 'me' menggunakan regex
        pattern = r'\bme\w*'
        me_words = re.findall(pattern, text, re.IGNORECASE)

        # Konversi list menjadi tuple
        me_words_tuple = tuple(me_words)

        return me_words_tuple

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return ()

# Testcase
file_path = 'indonesia.txt'
me_words = extract_me_words(file_path)

# ========================================================================

# Function untuk mengekstrak kata-kata yang dimulai dengan 'di'
def extract_di_words(file_path):
    try:
        # Buka file dan baca isinya
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Cari semua kata yang diawali dengan 'di' menggunakan regex
        pattern = r'\bdi\w+'
        di_words = re.findall(pattern, text, re.IGNORECASE)

        # Konversi list menjadi tuple
        di_words_tuple = tuple(di_words)

        return di_words_tuple

    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    return ()

file_path = 'indonesia.txt'
di_words = extract_di_words(file_path)

# ==============================================================================

# Function untuk mengekstrak kata-kata setelah 'di' dengan spasi
def extract_di_(file_path):
    try:
        # Buka file dan baca isinya
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Cari semua kemunculan 'di' dan mengambil kata setelahnya
        pattern = r'\bdi\s+\w+'
        di_words = re.findall(pattern, text)

        return di_words

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return []

file_path = 'indonesia.txt'
di_words2 = extract_di_(file_path)
# ==============================================================================

# Function untuk mengekstrak data dari tabel HTML
def extract_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Pola regex untuk mencari baris tabel yang mengandung nama negara dan nilai
        pattern = r'<tr>\s*<td align="left"><span class="flagicon">.*?<a href="https://en.wikipedia.org/wiki/([^"]+)"[^>]*>([^<]+)</a></td>\s*<td>([^<]+)</td>'
        data = re.findall(pattern, text, re.DOTALL)

        result = []
        for item in data:
            country = item[1]
            try:
                value = float(item[2].strip())
            except ValueError:
                value = (item[2].strip())
            result.append((country, value))

        return result
    
kei = extract_data('KEI.html')
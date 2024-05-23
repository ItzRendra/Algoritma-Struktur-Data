import math  # Mengimpor modul math untuk menggunakan fungsi-fungsi matematika

class Point:
    def __init__(self, x=0, y=0):
        # Konstruktor untuk menginisialisasi objek Point
        # Jika tidak diberikan nilai x dan y, maka titik akan berada di (0, 0)
        self.x = x
        self.y = y

    def set_location(self, x, y):
        # Metode untuk mengatur lokasi titik dengan nilai x dan y baru
        self.x = x
        self.y = y

    def distance_from_origin(self):
        # Metode untuk menghitung jarak titik dari titik asal (0, 0)
        # Menggunakan teorema Pythagoras
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other_point):
        # Metode untuk menghitung jarak antara titik saat ini dengan titik lain
        dx = self.x - other_point.x  # Selisih koordinat x
        dy = self.y - other_point.y  # Selisih koordinat y
        # Menggunakan teorema Pythagoras
        return math.sqrt(dx**2 + dy**2)


class Vehicle:
    def __init__(self, name, color, year_production, mileage):
        # Konstruktor untuk menginisialisasi objek Vehicle yang memiliki variable ; nama, color, year_production, mileage, dan capacity
        self.name = name
        self.color = color
        self.year_production = year_production
        self.mileage = mileage
        self.capacity = None

    def set_capacity(self, capacity):
        #fungsi untuk merubah capacity
        self.capacity = capacity

class Truck(Vehicle):
    #class Truck Inheritance dari Vehicle
    pass

def printInfo(self):
    #mencetak info instance/nama kendaraan
    print("\nNama Kendaraan : ", self.name)  # Output: nama dari class
    print("Warna Kendaraan : ", self.color)  # Output: color dari class
    print("Tahun Produksi : ", self.year_production)  # Output: yp dari class 
    print("Jarak Yang sudah di tempuh : ", self.mileage)  # Output: mileage dari class
    print("Kapasitas Kendaraan : ", self.capacity) # Output: capacity dari class


my_vehicle = Vehicle("Toyota Supra", "Black", 2020, 25000) #membuat objek dari vehicle
my_vehicle.set_capacity(5)
printInfo(my_vehicle)

my_truck = Truck("Ford", "Red", 2017, 10000) #membuat objek dari class Truck
my_truck.set_capacity(3)
printInfo(my_truck)





"""
Program : MenentukanGanjilGenap
{I.S. : pengguna memasukkan sebuah nilai ke dalam variable bilangan}
{F.S. : menampilkan hasil keterangan "Bilangan genap" atau "Bilangan Ganjil"}

Kamus :
    Bilangan    : integer
    Keterangan  : string
"""
# Input bilangan
Bilangan = int(input("Masukkan sebuah bilangan : "));

# ====MENGGUNAKAN ANALISIS SATU KASUS====
print("=====ANALISIS SATU KASUS=====");

# inisialisasi variable bilangan
Keterangan = "Bilangan ganjil";
if ((Bilangan % 2) == 0):
    Keterangan = "Bilangan genap";

# menampilkan hasil dari keterangan
print(f"{Bilangan} adalah {Keterangan}");

# ====MENGGUNAKAN ANALISIS DUA KASUS====
print("=====ANALISIS DUA KASUS=====");
if((Bilangan % 2) == 0):
    Keterangan = "Bilangan genap"
else:
    Keterangan = "Bilangan ganjil";

# menampilkan hasil dari keterangan
print(f"{Bilangan} adalah {Keterangan}");

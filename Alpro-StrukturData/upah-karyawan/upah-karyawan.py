"""
Program : UpahKaryawan
{I.S. : user memasukkan karyawan, upah dan jam kerja selama 1 minggu}
{F.S. : menampilkan nama karyawan, jam kerja, jam lembur dan upah total karyawan}
"""
import os;

# Memasukkan nama karyawan 
NamaKaryawan = str(input("Masukkan nama karyawan         : "));

# Memasukkan upah perjam
Upah        = int(input("Masukkan upah per jam          : "));

# Memasukkan jam kerja selama 1 minggu
JamKerja    = int(input("Lama jam kerja selama 1 minggu : "));

# Memasukkan upah total
UpahTotal   = (Upah * JamKerja);

# validasi jam kerja
if (JamKerja > 40):
    JamLembur       = JamKerja - 40;
    UpahLembur      = (2 * Upah * JamLembur);
    UpahTotal       = (Upah * (JamKerja - JamLembur)) + UpahLembur;

os.system("pause");
os.system("cls");
# menampilkan data karyawan
print("          DATA KARYAWAN");
print("="*33);
print(f"Nama karyawan               : {NamaKaryawan.upper()}");
print(f"Jam kerja dalam 1 minggu    : {JamKerja} jam");
print(f"Upah total yang diterima    : Rp{UpahTotal:,}");

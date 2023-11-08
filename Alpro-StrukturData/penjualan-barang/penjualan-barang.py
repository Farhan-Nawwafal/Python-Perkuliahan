"""
Program : PenjualanBarang
{I.S. : user memasukkan kode barang (KodeBrg), jumlah barang (Jumlah), pembayaran(Bayar)}
{F.S. : menampilkan kode barang, nama barang (NamaBrg), jumlah, harga satuan, harga total, diskon, total bayar, bayar, uang kembali}
"""

import os

# memasukkan kode barang
KodeBrg = str(input("Masukkan Kode Barang             : ")).upper();
# validasi kode barang
if((KodeBrg != "PK01") and (KodeBrg != "TS02") and (KodeBrg != "SP03") and (KodeBrg != "AK04")):
    print("Salah memasukkan kode barang!");
else:
    # memasukkan jumlah barang yang dibeli
    Jumlah = int(input("Masukkan jumlah barang           : "));

    # inisialisasi besar diskon
    BesarDiskon = 0;

    # validasi jumlah jika jumlah > 0.5 * kodi (1 kodi = 20 buah)
    if(Jumlah >= 10):
        # Memasukkan ada diskon atau ga
        AdaDiskon = str(input("Ada diskon atau ga ? [Ya/Tidak]  : "));
        
        # validasi ada diskon atau ga
        if(AdaDiskon == "Ya"):
            # Memasukkan besar diskon
            BesarDiskon = float(input("Masukkan besar diskonnya         : "));

# Menentukan nama barang dan harga satuan
if (KodeBrg == "PK01"):
    NamaBrg     = "Pakaian";
    HargaSatuan = 75000;
elif (KodeBrg == "TS02"):
    NamaBrg     = "Tas";
    HargaSatuan = 65000;
elif (KodeBrg == "SP03"):
    NamaBrg     = "Sepatu";
    HargaSatuan = 157000;
elif (KodeBrg == "AK04"):
    NamaBrg     = "Aksesoris";
    HargaSatuan = 45000;

# menghitung harga total
HargaTotal = (HargaSatuan * Jumlah);

# menentukan diskon
Diskon = 0;
if(BesarDiskon != 0):
    Diskon = (BesarDiskon/100) * HargaTotal;

# menghitung total bayar
TotalBayar = HargaTotal - Diskon;

# Input harga bayar
Bayar = int(input("Masukkan uang pembayaran kamu    : "));


# validasi uang bayar
if(Bayar < TotalBayar):
    print("Maaf! Uang kamu kurang. Isi lagi!");
    Bayar = int(input("Masukkan uang pembayaran kamu    : "));

# menghitung uang kembalian
Kembali = Bayar - TotalBayar;

os.system("pause");
os.system("cls");

# menampilkan data yang dibeli beserta total bayar
print("LAYAR MASUKAN");
print("-------------");
print(f"Kode Barang             : {KodeBrg}");
print(f"Jumlah beli             : {Jumlah} pcs");
print(f"Ada Diskon [Ya/Tidak]   : {AdaDiskon}");
print(f"Besar Diskon(%)         : {BesarDiskon}");

print("LAYAR KELUARAN");
print("--------------");
print(f"Kode Barang             : {KodeBrg}");
print(f"Nama Barang             : {NamaBrg}");
print(f"Jumlah Beli             : {Jumlah}");
print(f"Harga Satuan            : Rp{HargaSatuan:,}");
print(f"Harga Total             : Rp{HargaTotal:,}");
if(BesarDiskon != 0):
    print(f"Diskon {BesarDiskon}%            : Rp{Diskon:,}");
else :
    print(f"Diskon {BesarDiskon}%               : Rp{Diskon:,}");
print(f"Total Bayar             : Rp{TotalBayar:,}")
print("---------------------------------------");
print(f"Bayar                   : Rp{Bayar:,}");
print(f"Uang Kembali            : Rp{Kembali:,}");







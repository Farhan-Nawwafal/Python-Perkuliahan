"""
PenggajianKaryawan
{I.S. : user masukkan bulan, tahun, tiga buah NIK, nama karyawan dan 3 buah gaji pokok}
{F.S. : menampilkan pajak, tunjangan, gaji bersih perkaryawan beserta gaji bersih}

Kamus : 
    bulan, tahun, NIK1, NIK2, NIK3, nama1, nama2, nama3 : string;
    gajiPokok1, gajiPokok2, gajiPokok3 : integer;
    pajak1, pajak2, pajak3, tunjangan1, tunjangan2, tunjangan3, gajiBersih1, gajiBersih2, gajiBersih3, gajiTotal : real; 

Algoritma : 
    Input(bulan, tahun, NIK1, nama1, gajiPokok1, NIK2, nama2, gajiPokok2, NIK3, nama3, gajiPokok3)
    pajak1 <-- 0.1 * gajiPokok1
    pajak2 <-- 0.1 * gajiPokok2
    pajak3  <-- 0.1 * gajiPokok1
    tunjangan1 <-- 0.2 * gajiPokok1 
    tunjangan2 <-- 0.2 * gajiPokok2 
    tunjangan3 <-- 0.2 * gajiPokok3
    gajiBersih1 <-- gajiPokok1 + tunjangan1 - pajak1
    gajiBersih2 <-- gajiPokok2 + tunjangan2 - pajak2
    gajiBersih3 <-- gajiPokok3 + tunjangan3 - pajak3
    totalGaji <-- gajiBersih1 + gajiBersih2 + gajiBersih3
    output(pajak1, pajak2, pajak3, tunjangan1, tunjangan2, tunjangan3, gajiBersih1, gajiBersih2, gajiBersih3, totalGaji)
"""

import os

# memasukkan bulan dan tahun penggajian
bulan = str(input("Masukkan nama bulan : "));
tahun = str(input("Masukkan tahun : "));

# memasukkan 3 buah nama, 3 buah nik dan 3 gajipokok
print("MASUKKAN DATA KARYAWAN");
print("----------------------");
print("<< Data Karyawan Ke-1 >>");
NIK1        = str(input("Masukkan NIK anda              : "));
nama1       = str(input("Masukkan nama karyawan         : "));
gajiPokok1  = int(input("Masukkan gaji pokok karyawan   : Rp. "));

print("\n");

print("<< Data Karyawan Ke-2 >>");
NIK2        = str(input("Masukkan NIK anda              : "));
nama2       = str(input("Masukkan nama karyawan         : "));
gajiPokok2  = int(input("Masukkan gaji pokok karyawan   : Rp. "));

print("\n");

print("<< Data Karyawan Ke-3 >>");
NIK3        = str(input("Masukkan NIK anda              : "));
nama3       = str(input("Masukkan nama karyawan         : "));
gajiPokok3  = int(input("Masukkan gaji pokok karyawan   : Rp. "));

# menghitung pajak 3 karyawan
pajak1 = 0.1 * gajiPokok1;
pajak2 = 0.1 * gajiPokok2;
pajak3 = 0.1 * gajiPokok3;

# menghitung tunjangan 3 karyawan
tunjangan1 = 0.2 * gajiPokok1;
tunjangan2 = 0.2 * gajiPokok2;
tunjangan3 = 0.2 * gajiPokok3;

# menghitung gaji bersih 3 karyawan
gajiBersih1 = gajiPokok1 + tunjangan1 - pajak1;
gajiBersih2 = gajiPokok2 + tunjangan2 - pajak2;
gajiBersih3 = gajiPokok3 + tunjangan3 - pajak3;

# menghitung total gaji
totalGaji = gajiBersih1 + gajiBersih2 + gajiBersih3

# menampilkan laporan penggajian
os.system('cls');
print("                                     Laporan Penggajian");
print("                                     ------------------");
print(f"bulan/tahun : {bulan}/{tahun}");
print("------------------------------------------------------------------------------------------");
print("|    NIK    | Nama Karyawan |  Gaji Pokok  |    Tunjangan1 |     Pajak     | Gaji Bersih    | ");
print("------------------------------------------------------------------------------------------");
print(f"| {NIK1:9} | {nama1:13} | Rp. {gajiPokok1:8} | Rp. {tunjangan1:8.1f} | {pajak1:8.1f} | {gajiBersih1:12.1f}");
print(f"| {NIK2:9} | {nama2:13} | Rp. {gajiPokok2:8} | Rp. {tunjangan2:8.1f} | {pajak2:8.1f} | {gajiBersih2:12.1f}");
print(f"| {NIK3:9} | {nama3:13} | Rp. {gajiPokok3:8} | Rp. {tunjangan3:8.1f} | {pajak3:8.1f} | {gajiBersih3:12.1f}");
print("------------------------------------------------------------------------------------------");
print(f"Total gaji : Rp. {totalGaji:10.1f}");
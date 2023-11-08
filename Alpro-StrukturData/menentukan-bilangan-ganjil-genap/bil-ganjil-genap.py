"""
Program : Menentukan bilangan ganjil atau genap.

MenentukanBilanganGanjilGenap
{I.S. : user memasukkan bilangan sembarang}
{F.S. : menampilkan hasil dari inputan user}

Kamus       :
    bilangan    : integer
    keterangan  : string    {untuk memberi keterangan bilangan}

Algoritma   :
    Input(bilangan)
    
    if (bilangan mod 2 = 0) then
        keterangan <-- "Ini adalah bilangan genap"
        Output(keterangan)
    else 
        keterangan <-- "Ini adalah bilangan ganjil"
        Output(keterangan)
"""
# membuat variable bilangan
bilangan = int(input("Masukkan sembarang bilangan : "))

if ((bilangan % 2) == 0):
    keterangan = "Ini adalah bilangan genap"
    print(keterangan)
else:
    keterangan = "Ini adalah bilangan ganjil"
    print(keterangan);
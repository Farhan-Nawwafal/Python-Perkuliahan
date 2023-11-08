"""
MenghitungLuasLingkaran
{I.S. : user memasukkan diameter lingkaran dalam satuan cm, lalu akan dikonversi ke dalam satuan meter}
{F.S. : menampilkan hasil hasil luas lingkaran}

Kamus :
    diameterCm : integer {diameter dalam satuan cm}
    diameterM, LuasLingkaran : real {diameter dalam satuan m}

Algoritma :
    input(diameterCm) 
    diameterM <-- (diameterCm)/100
    LuasLingkaran <-- (3.14 * sqr(diameterM))/4
    Output(LuasLingkaran)
"""

# user memasukkan diameter dalam satuan cm
diameterCm = int(input("Masukkan nilai diameter cm : "));

# mengubah diameter satuan cm ke meter
diameterM = (diameterCm) / 100;

# masukkan rumus luas lingkaran 
luasLingkaran = (3.14 * (diameterM)** 2)/4

# tampilkan hasil luasLingkaran
print(f"Hasil luas lingkaran berdiameter {diameterM} m adalah : {luasLingkaran:.2f} m persegi");

# a = 3
# print("Nilai a adalah : ", a)
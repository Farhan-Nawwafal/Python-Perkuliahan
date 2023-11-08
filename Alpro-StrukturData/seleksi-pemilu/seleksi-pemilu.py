"""
Program : SeleksiPemilu
{I.S. : user memasukkan umur dan status menikah}
{F.S. : menampilkan boleh memilih atau tidak}
"""
# Memasukkan umur 
Umur = int(input("Masukkan umur Anda : "));

# Menentukan boleh memilih atau tidak
if(Umur < 17):
    Menikah = str(input("Apakah Anda sudah menikah [Y/T] ? : ")).upper();
    # Ini pake if
    """
    if(Menikah == "Y"):
        print("Anda boleh ikut pemilu");
    else:
        print("Anda tidak boleh mengikuti pemilu");
    """
    # menyederhanakan bentuk if
    match(Menikah):
        case "Y" : print("Anda boleh mengikuti pemilu");
        case "T" : print("Anda tidak boleh mengikuti pemilu");
        case _: print("Hanya boleh \"Y\" atau \"T\" !");
else:
    print("Anda boleh ikut pemilu");
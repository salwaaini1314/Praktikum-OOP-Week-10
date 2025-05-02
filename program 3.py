class Pengiriman:
    def argo(self):
        pass

class Dalam_Kota(Pengiriman):
    def argo(self):
        print("\n=> Pengiriman ke wilayah kota akan dikirim menggunakan Grab")

class Luar_Kota(Pengiriman):
    def argo(self):
        print("\n=> Pengiriman ke luar kota akan dikirim menggunakan JNE")

class Factory:
    @staticmethod
    def pilih(tujuan):
        if tujuan == "dalam kota":
            return Dalam_Kota()
        elif tujuan == "luar kota":
            return Luar_Kota()
        else:
            raise ValueError("Tujuan yang anda masukkan tidak valid")
        
tujuan = input("Paket akan dikirim ke mana [luar kota/dalam kota]? ").lower()
paket = Factory.pilih(tujuan)
paket.argo()
class KatakZuma:
    def __init__(self, warna_awal):
        #inisialisasi atribut objek
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        #mengubah warna peluru dengan warna yg baru
        self.warna_peluru = warna_baru
        self.load_gambar(warna_baru)

    def load_gambar(self, warna):
        #mekanisme untuk memuat gambar
        pass

    def tembak(self, jumlah_bola_sama):
        #skor bertambah hanya ketika minimal ada 3 bola yg berwarna sama
        if jumlah_bola_sama >= 3:
            print(f"berhasil, ada {jumlah_bola_sama} bola warna {self.warna_peluru} yang hancur")
            self.skor += 50 * jumlah_bola_sama  
        else:
            print(f"gagal, cuma ada {jumlah_bola_sama} bola")

    def info_status(self):
        #menampilkan informasi status katak saat ini
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Skor : {self.skor}")
        print(f"Status : {self.is_active}")

# --- UJI COBA PROGRAM ---

katak_player = KatakZuma("Kuning")

print("Kondisi Awal:")
katak_player.info_status()
print()

#mencoba menembak saat bola yg sama hanya ada 2, hasilnya poin blm bertambah atau gagal
katak_player.ganti_warna("Merah")
katak_player.tembak(2) 

print()
#mencoba menembak saat bola yg sama ada 3, hasilnya poin bertambah karena udah masuk kedalam syarat minimal
katak_player.tembak(3) 

print()
print("Kondisi Akhir:")
katak_player.info_status()
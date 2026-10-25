class KarakterSurfer:
    def __init__(self, nama):
        # inisialisasi properties awal karakter
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # mengubah status karakter menjadi mulai berlari
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        # menambahkan koin yang diambil
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin.")

    def tabrak_rintangan(self):
        # mengubah status menjadi berhenti jika menabrak rintangan
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Game Over.")

    def info_player(self):
        # menampilkan informasi player saat ini
        print(f"Nama Player : {self.nama}")
        print(f"Skor        : {self.skor}")
        print(f"Jumlah Koin : {self.koin}")
        print(f"Status Lari : {self.is_running}")

# --- PENGUJIAN OBJEK ---
# membuat objek player1
player1 = KarakterSurfer("Jake")

# menampilkan informasi awal player1
player1.info_player()
print()

# mencoba menjalankan beberapa aksi
player1.berlari()
player1.ambil_koin(15)
player1.ambil_koin(10)
player1.tabrak_rintangan()

print()
# menampilkan informasi player1 setelah selesai bermain
player1.info_player()
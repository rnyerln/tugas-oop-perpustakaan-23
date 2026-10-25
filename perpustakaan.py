class Perpustakaan:
    def __init__(self, nama_peminjam, judul_buku, durasi_pinjam):
        # inisialisasi properties awal peminjaman
        self.nama_peminjam = nama_peminjam
        self.judul_buku = judul_buku
        self.durasi_pinjam = durasi_pinjam
        self.is_active = True

    def pinjam_buku(self):
        # mengubah status menjadi aktif/dipinjam dan menampilkan informasi
        self.is_active = True
        print(f"{self.nama_peminjam} berhasil meminjam buku '{self.judul_buku}' selama {self.durasi_pinjam} hari.")

    def perpanjang_waktu(self, tambahan_hari):
        # menambah durasi pinjam buku
        self.durasi_pinjam += tambahan_hari
        print(f"Masa peminjaman {self.nama_peminjam} diperpanjang {tambahan_hari} hari. Total durasi pinjam: {self.durasi_pinjam} hari.")

    def kembalikan_buku(self):
        # mengubah status menjadi tidak aktif/dikembalikan
        self.is_active = False
        print(f"Buku '{self.judul_buku}' telah dikembalikan oleh {self.nama_peminjam}. Status aktif: {self.is_active}")

    def info_peminjaman(self):
        # menampilkan informasi peminjaman saat ini
        print(f"Nama Peminjam : {self.nama_peminjam}")
        print(f"Judul Buku    : {self.judul_buku}")
        print(f"Durasi Pinjam : {self.durasi_pinjam} hari")
        print(f"Status Aktif  : {self.is_active}")

# --- PENGUJIAN OBJEK ---
# membuat objek peminjam1
peminjam1 = Perpustakaan("Karina", "belajar pemrograman OOP", 7)

# menampilkan informasi awal peminjaman
peminjam1.info_peminjaman()
print()

# mencoba menjalankan beberapa aksi
peminjam1.perpanjang_waktu(3)
print()
peminjam1.kembalikan_buku()

print()
# menampilkan informasi setelah buku dikembalikan
peminjam1.info_peminjaman()
class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            self.inventori[nama_barang] += jumlah
        else:
            self.inventori[nama_barang] = jumlah
        return f"Berhasil menambahkan {jumlah} stok {nama_barang}."

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            if self.inventori[nama_barang] >= jumlah:
                self.inventori[nama_barang] -= jumlah
                return f"Berhasil mengurangi/menghapus {jumlah} stok {nama_barang}."
            else:
                return f"Stok {nama_barang} tidak mencukupi."
        return f"Barang {nama_barang} tidak ditemukan di inventori."

    def lihat_inventori(self):
        return f"Daftar Inventori Saat Ini: {self.inventori}"

# Testing / Demonstrasi Method
gudang = ManajerInventori()
print(gudang.tambah_barang("Laptop ASUS", 10))
print(gudang.tambah_barang("Mouse Logitech", 25))
print(gudang.hapus_barang("Laptop ASUS", 3))
print(gudang.lihat_inventori())
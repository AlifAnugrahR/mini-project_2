print("Nama : Alif Anugrah Ramadhan")
print("Nim  : 2509116019")
print("kelas: Sistem informasi 25")
print("tugas: Mini Project 2")
print("Aslab: Bang Dharma dan Bang Zyrus")

akun = {
    "hajialif": {"password": "senggol dong", "role": "Manager"},
    "karyawan": {"password": "sayasuka ddp", "role": "Karyawan"}
}

inventaris = {
    "latte"       :{"jumlah": 10, "harga": 15000},
    "matcha"      :{"jumlah": 82, "harga": 18000},
    "caramel"     :{"jumlah": 54, "harga": 20000},
    "kopi alpukat":{"jumlah": 71, "harga": 20000},
    "kopi melon"  :{"jumlah": 57, "harga": 12000}
}

def lihat_barang():
    print("\nDAFTAR BARANG ")

    if not inventaris:
        print("Kosong... sama kayak hati waktu ditinggalin.")
    else:
        for i, (nama, data) in enumerate(inventaris.items(), start=1):
            print(f"{i}. {nama.title()} | Jumlah: {data['jumlah']} | Harga: Rp{data['harga']}")
    print("-"*45)

def tambah_barang():
    try:
        nama = input("Mau nambah barang apa pak HAJIII?: ").lower()
        if nama in inventaris:
            print("upss barang ini udah ad pak hajiii")
            return
        jumlah = int(input("Masukkan jumlahnya : "))
        harga = int(input("Masukkan harganya : "))
        inventaris[nama] = {"jumlah": jumlah, "harga": harga}
        print(f"Barang '{nama}' berhasil ditambahkan, kelazz barang baru")
    except ValueError:
        print("Salah input PAK HAJIII")
"-"*45

def update_barang():
    lihat_barang()
    nama = input("YOWW PAK HAJI mau perbarui apa? : ").lower()
    if nama not in inventaris:
        print("Barang gak ketemu boss... kayak dia yang udah gak bisa dicari lagi")
        return
    try:
        jumlah = int(input("jumlah baru : "))
        harga = int(input("harga baru : "))
        inventaris[nama] = {"jumlah": jumlah, "harga": harga}
        print(f"Barang '{nama}' berhasil diperbarui")
    except ValueError:
        print("Input salahhh pak haji")
"-"*45

def hapus_barang():
    lihat_barang()
    nama = input("haii pak haji mau hapus yg mana? : ").lower()
    if nama in inventaris:
        del inventaris[nama]
        print(f"Barang '{nama}' sudah dsingkirkan pak haji")
    else:
        print("waddduh barang nya ga ada pak hajii")
"-"*45

def login():
    while True:
        try:
            print("\nsilahkan loginnn boss")
            username = input("Username (isi dengan jelas):").lower()
            password = input("Password (jangan lupa, jan kayak dia lupa janji): ")
            if username in akun and akun[username]["password"] == password:
                print(f"Login berhasil... selamat datang {akun[username]['role']}, jangan pergi ya.\n")
                return akun[username]["role"]
            else:
                print("Username atau password salahh ganteng\n")
        except KeyboardInterrupt:
            print("\nProgram dihentikan secara paksa pakai Ctrl+C... kayak hubungan admin")
            exit()

def menu_manager():
    print("\nMENU MANAGER (Haji Alif) ")
    print("1. Lihat barang ")
    print("2. Tambah barang ")
    print("3. Update barang ")
    print("4. Hapus barang ")
    print("5. Logout ")

def menu_karyawan():
    print("\n=== MENU KARYAWAN ===")
    print("1. Lihat barang ")
    print("2. Logout ")

def main():
    try:
        while True:
            role = login()
            while True:
                if role == "Manager":
                    menu_manager()
                else:
                    menu_karyawan()
                pilihan = input("Pilih menu : ")
                if pilihan == "1":
                    lihat_barang()
                elif pilihan == "2" and role == "Manager":
                    tambah_barang()
                elif pilihan == "3" and role == "Manager":
                    update_barang()
                elif pilihan == "4" and role == "Manager":
                    hapus_barang()
                elif pilihan == "5":
                    print("Logout berhasil...move on yg ga berhasil :(")
                    break
                else:
                    print("Pilihan gak cocok atau ga valid.. ")
    except KeyboardInterrupt:
        print("\nProgram dihentikan secara paksa pakai Ctrl+C... kayak hubungan pak haji ahahahahah")

if __name__ == "__main__":
    main()

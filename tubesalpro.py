# import library matplolib untuk visualisasi data yang digunakan
import matplotlib.pyplot as plt

# fungsi untuk pemesanan tiket kereta antar kota
def antarkota():
    ka = 0
    dataumur = []
    datanama = []
    while True:
        print("""
        Selamat Datang Di Layanan Pembelian Kereta Api Antar Kota :
        1. Pesan Tiket Kereta Api Antar Kota
        2. Visualisasi Data dalam Pembelian Tiket Kereta Api Antar Kota
        0. Keluar dari Layanan Pembelian Kereta Api Antar Kota
        """)
        pilih = int(input("Masukkan Layanan yang Anda inginkan :  "))

        if pilih == 1 :
            nama = input("Masukkan Nama Anda                : ")
            datanama.append(nama)
            tgl = input("Masukkan Tanggal Keberangkatan     : ")
            umur = int(input("Masukkan umur Anda            : "))
            dataumur.append(umur)
            qty = int(input("Masukkan Jumlah Penumpang      : "))
            pergi = input("""Pilih Nomor Stasiun Tujuan     :
            1.  Stasiun Bandung -  Stasiun Gambir
            2.  Stasiun Bandung - Stasiun Tasikmalaya         
            3.  Stasiun Bandung - Stasiun Yogyakarta
            4.  Stasiun Bandung - Stasiun Gubeng
            Masukkan Nomor Stasiun Keberangkatan yang dipilih : 
            """)

            if pergi == "1":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Gambir Jakarta")
                tujpilih = "Stasiun Bandung - Stasiun Gambir Jakarta"

            elif pergi == "2":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Tasikmalaya")
                tujpilih = "Stasiun Bandung - Stasiun Tasikmalaya"

            elif pergi == "3":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Yogyakarta")
                tujpilih = "Stasiun Bandung - Stasiun Yogyakarta"

            elif pergi == "4":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Gubeng Surabaya")
                tujpilih = "Stasiun Bandung - Stasiun Gubeng Surabaya"

            else:
                print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")

            kelas = input("""Silahkan pilih Nomor Kelas yang Tersedia : 
                1. Ekonomi (Rp 80.000)
                2. Bisnis (Rp 135.000)
                3. Eksekutif (Rp. 170.000)
                Masukkan Nomor Kelas yang dipilih : 
                """)
            if kelas == "1":
                print("Anda Telah Memilih Kelas Ekonomi")
                kelaspilih = "Ekonomi"
                ka1 = 80000
                ka += ka1

            elif kelas == "2":
                print("Anda Telah Memilih Kelas Bisnis")
                kelaspilih = "Bisnis"
                ka2 = 135000
                ka += ka2

            elif kelas == "3":
                print("Anda Telah Memilih Kelas Eksekutif")
                kelaspilih = "Eksekutif"
                ka3 = 170000
                ka += ka3

            else:
                print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")
            hrgtotal = ka * qty

            print(f"""
            Booking dengan Nama {nama} dan umur {umur} berhasil dipesan!
            Nama                    : {nama}      
            Tanggal Booking         : {tgl}
            Jumlah Penumpang        : {qty} Orang
            Keberangkatan - Tujuan  : {tujpilih} 
            Kelas Yang Dipilih      : {kelaspilih}
            Rincian Biaya           : Rp {hrgtotal}
            """)

        elif pilih == 2:

            print(datanama,dataumur)
            
            plt.plot(datanama,dataumur, label="2020", color="green",
                        marker="o", markerfacecolor = "black")
            plt.xlabel("Nama Pembeli")
            plt.ylabel("Umur Pembeli")
            plt.ticklabel_format(style="plain", axis="y")

            plt.title("Grafik Nama dan Umur Pembeli Tiket Kereta Api Antar Kota")

            plt.show()

        elif pilih == "0":
            print("Terima Kasih telah menggunakan Layanan Pembelian Tiket Kereta Api Antar Kota")
            break
        
        else :
            print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")
            break


# fungsi untuk penggunaan ewallet KAIPayment
def kaipay():
    global plt
    data = []
    pembelian = []
    awal = 0
    while True:
        print("""
        Selamat Datang Di Layanan KAIPayment :
        (Note : Sebelum Anda Mulai Mohon Top Up saldo Terlebih Dahulu)
        1. Top Up Saldo KAIPayment
        2. Cek Saldo KAIPayment Saat Ini
        3. Mengurutkan Riwayat Top Up Saldo 
        4. Cek Jumlah Saldo yang Pernah Di Top Up
        5. Visualisasi data anda dalam menggunakan KAIPayment
        0. Keluar dari Layanan KAIPayment
        """)
        pilih = input("Masukkan Layanan yang Anda inginkan :  ")
        if pilih == "1":
            sld = int(
                input("Masukkan Nominal Saldo yang Ingin anda Top Up : Rp "))
            print(f"Saldo sebesar Rp{sld} berhasil ditopup!")
            awal += 1
            data.append(sld)
            pembelian.append(awal)

        elif pilih == "2":
            ttl = sum(data)
            print(f"Jumlah Saldo Saat Ini Rp {ttl} ")

        elif pilih == "3":
            print("Saldo Yang Pernah Di Top Up : ")
            for i in range(len(data)):
                print(f"{i+1} .Rp {data[i]}")

        elif pilih == "4":
            data.sort(reverse=True)
            print("Saldo yang pernah di topup telah diurutkan")

        elif pilih == "5":
            print(pembelian,data)

            plt.plot(pembelian, data, label="2020", color="green",
                     marker="o", markerfacecolor="black")
            plt.xlabel("Pembelian ke-")
            plt.ylabel("Banyaknya pembelian")
            plt.ticklabel_format(style="plain", axis="y")

            plt.title("Jumlah data pembelian saldo user")

            plt.show()

        elif pilih == "0":
            print("Terima Kasih telah menggunakan layanan KaiPayment.")
            break
        else:
            print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")


# fungsi untuk pemesanan tiket kereta api lokal
def kalokal():
    ka = 0
    dataumur = []
    datanama = []    
    hrg = 25000
    
    while True:
        print("""
        Selamat Datang Di Layanan Pembelian Kereta Api Lokal :
        1. Pesan Tiket Kereta Api Lokal
        2. Cetak Pesanan Tiket Kereta Api Lokal Anda
        0. Keluar dari Layanan Pembelian Kereta Api Lokal
        """)
        pilih = int(input("Masukkan Layanan yang Anda inginkan :  "))
        
        if pilih == 1:
            nama = input("Masukkan Nama Anda                    : ")
            tgl = input("Masukkan Tanggal Keberangkatan         : ")
            umur = int(input("Masukkan Umur Anda                : "))
            qty = int(input("Masukkan Jumlah Penumpang          : "))
            pergi = input("""Pilih Nomor Stasiun Tujuan         :
            1.  Stasiun Bandung -  Stasiun Cicalengka
            2.  Stasiun Bandung - Stasiun Cimahi         
            3.  Stasiun Bandung - Stasiun Cimindi
            4.  Stasiun Bandung - Stasiun Rancaekek
            Masukkan Nomor Stasiun Keberangkatan yang dipilih   : 
            """)
            print(f"Harga Tiket : {hrg} ")

            if pergi == "1":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Cicalengka")
                tujpilih = "Stasiun Bandung - Stasiun Cicalengka"

            elif pergi == "2":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Cimahi")
                tujpilih = "Stasiun Bandung - Stasiun Cimahi"            

            elif pergi == "3":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Cimindi")
                tujpilih = "Stasiun Bandung - Stasiun Cimindi"

            elif pergi == "4":
                print("Anda telah memilih Kereta Stasiun Bandung menuju Stasiun Rancaekek")
                tujpilih = "Stasiun Bandung - Stasiun Rancaekek"

            else:
                print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")

            hrgtotal = hrg*qty

            print(f"""
            Booking dengan Nama {nama} dan Umur {umur} berhasil dipesan!
            Nama                    : {nama}      
            Tanggal Booking         : {tgl}
            Jumlah Penumpang        : {qty} Orang
            Keberangkatan - Tujuan  : {tujpilih} 
            Rincian Biaya           : Rp {hrgtotal}
            """)

        elif pilih == 2:
            print("Bukti Pesanan telah dicetak, silahkan cek perangkat Anda!")
            data = (f"Booking dengan Nama {nama} dan umur {umur} berhasil dipesan!\nNama                    : {nama}\nTanggal Booking         : {tgl}\nJumlah Penumpang        : {qty} Orang\nKeberangkatan - Tujuan  : {tujpilih}\nRincian Biaya           : Rp {hrgtotal}")
            data_file = open("Bukti Pemesanan.txt","a")
            data_file.write(data)
            data_file.close
            break

        elif pilih == 0:
            print("Terima Kasih telah menggunakan Layanan Pembelian Tiket Kereta Api Lokal")
            break
        
        else :
            print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")

        
# Menu utama program
while True:
    try:
        print("""
    ==== Selamat Datang di Layanan Akses Kereta Api Indonesia ! =====
    Berikut ini Daftar Menu yang Tersedia :
    1. Tiket Kereta Antar Kota
    2. Tiket Kereta Lokal
    3. KAIPayment 
    0. Keluar
    """)
        menu = int(input("Pilih Nomor Menu Yang Anda Inginkan     : "))
        if menu == 1:
            antarkota()
        elif menu == 2:
            kalokal()
        elif menu == 3:
            kaipay()
        elif menu == 0:
            print("Terima Kasih telah menggunakan layanan Akses Kereta Api Indonesia")
            break
        else:
            print("Fungsi Tidak Tersedia, Silahkan masukkan nomor yang dipilih")
    except ValueError:
        print("Program ini hanya menerima jenis nilai Integer!")
    except TypeError:
        print("Tipe data yang digunakan tidak sesuai!")
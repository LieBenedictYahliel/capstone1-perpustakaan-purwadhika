#Menu login
def login (user_id="",password=""):
    while True:
        print("Selamat datang di data peminjaman buku Perpustakaan Kami")
        print("1. Register")
        print("2. Login")
        register_or_login=input("Massukan angka yang ingin diakses(Login jika sudah register): ")
        if not register_or_login.isdigit():
            print("Input yang anda masukkan tidak sesuai dengan petunjuk: ")
            continue
        else:
            register_or_login_integer=int(register_or_login)
        if register_or_login_integer==1:
            username_register=(input("Silahkan masukkan User ID: "))
            Password_register=(input("Silahkan masukkan password: "))
            user_id=username_register
            password=Password_register
            print(f"{user_id} Sudah berhasil register")
            continue
        elif register_or_login_integer==2:
            while True:
                username_login = input("Silahkan masukkan User ID: ")
                Password_login = input("Silahkan masukkan password: ")
                if username_login!=user_id or Password_login!=password:
                    continue
                elif username_login==user_id and Password_login==password: 
                    print(f"Selamat datang {user_id} di Perpustakaan kami")
                    break
        return username_login,Password_login




#Membuat List buku
index_peminjam=[]
judul_buku=[]
nama_pengarang=[]
penerbit=[]
tahun_terbit=[]
genre_buku=[]
jumlah_halaman=[]
nama_peminjam=[]
def list_buku(nama_tabel=""):
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    for i in range(len(judul_buku)):
        index_peminjam = str(tahun_terbit[i])[2:]+judul_buku[i][:1].lower()+nama_peminjam[i][:2].upper()+str(tahun_terbit[i])[:2]  
        
        #input index peminjam untuk tabel data buku
        if nama_tabel=="judul_buku":
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}")
            print(f"{index_peminjam:<12}\t|{judul_buku[i]:<15}")
        
        elif nama_tabel=="nama_pengarang":
            print(f"{'Book ID':<12}\t|{'Nama Pengarang':<10}")
            print(f"{index_peminjam:<12}\t|{nama_pengarang[i]:<10}")
        
        elif nama_tabel=="penerbit":
            print(f"{'Book ID':<12}\t|{'Penerbit':<10}")
            print(f"{index_peminjam:<12}\t|{penerbit[i]:<10}")
        
        elif nama_tabel=="tahun_terbit":
            print(f"{'Book ID':<12}\t|{'Tahun Terbit':<10}")
            print(f"{index_peminjam:<12}\t|{tahun_terbit[i]:<10}")
        
        elif nama_tabel=="genre_buku":
            print(f"{'Book ID':<12}\t|{'Genre Buku':<10}")
            print(f"{index_peminjam:<12}\t|{genre_buku[i]:<10}")
        
        elif nama_tabel=="jumlah_halaman":
            print(f"{'Book ID':<12}\t|{'Jumlah Halaman':<10}")
            print(f"{index_peminjam:<12}\t|{jumlah_halaman[i]:<10}")
        
        elif nama_tabel=="nama_peminjam":
            print(f"{'Book ID':<12}\t|{'Nama Peminjam':<10}")
            print(f"{index_peminjam:<20}\t|{nama_peminjam[i]:<10}")
        
        else:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}\t|{'Penerbit':<10}\t|{'Tahun Terbit':<10}\t|{'Genre Buku':<10}\t|Jumlah Halaman\t|{'Nama Peminjam':<10}")
            print(f"{index_peminjam:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}\t|{penerbit[i]:<10}\t|{tahun_terbit[i]:<10}\t|{genre_buku[i]:<10}\t|{jumlah_halaman[i]:<10}\t|{nama_peminjam[i]:<10}")





#menu 1
#List menu perpustakaan    
def tittle_peminjamanan_buku_perpustakaan():
    menu_name="                     Data Peminjaman Buku Perpustakaan"
    print(menu_name.title())

def menu_utama_perpustakaan(): 
    tittle_peminjamanan_buku_perpustakaan()
    list_1_hingga_5_menu_perpustakaan=[
        "1. Menambah Buku",
        "2. Mengurangi Buku",
        "3. Pencarian Buku",
        "4. Biaya Peminjaman Buku",
        "5. Exit Program"
    ]
    print("Menu utama perpustakaan")
    for i in list_1_hingga_5_menu_perpustakaan:
        print(i)
    
    while True:
        pilihan_angka=input("Masukkan pilihan dengan angka(1-5): ")
        if pilihan_angka in ("1","2","3","4","5"):
            pilihan_angka_int=int(pilihan_angka)
            break
        else:
            print("Input tidak sesuai dengan petunjuk!")
    
    while True:
        if pilihan_angka_int==1:
            menu_menambah_buku()
            break
        elif pilihan_angka_int==2:
            menghapus_data()
            break
        elif pilihan_angka_int==3:
            menu_pencarian_buku()
            break
        elif pilihan_angka_int==4:
            konfirmasi_nama_peminjam_dan_denda()
            break
        elif pilihan_angka_int==5:
            print("Terima Kasih telah menggunakan service kami")
            break
        else:
            print("Input tidak sesuai dengan petunjuk!")
    return pilihan_angka_int   

#List Definition untuk menu utama buku
def menu_menambah_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam

    judul_buku_input=input("Masukkan Judul Buku: ").lower()
    nama_pengarang_input=input("Masukkan Nama Pengarang: ").lower()
    penerbit_input=input("Masukkan Penerbit: ").lower()
    def tahun_terbit_input():
        while True:
            int_tahun_terbit=input("Masukkan tahun terbit buku: ")
            if not int_tahun_terbit.isdigit():
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
            else:
                tahun_int_terbit=int(int_tahun_terbit)
                break
        return tahun_int_terbit
    tahun_terbit_input_bukan_list=tahun_terbit_input()
    genre_buku_input=input("Masukkan Genre Buku:").lower()
    def jumlah_halaman_input():
        while True:
            int_jumlah_halaman=input("Masukkan Jumlah Halaman: ")
            if int_jumlah_halaman.isdigit():
                return int(int_jumlah_halaman)
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")   
    jumlah_halaman_input_bukan_list=jumlah_halaman_input()       
    nama_peminjam_input=input("Masukkan Nama peminjam: ").lower()
    Index_peminjam_input=str(tahun_terbit_input_bukan_list)[2:]+judul_buku_input[:1].lower()+nama_peminjam_input[:2].upper()+str(tahun_terbit_input_bukan_list)[:2]
    
    index_peminjam.append(Index_peminjam_input) #menambah index peminjam input sesuai rumus ke dalam index peminjam
    judul_buku.append(judul_buku_input)
    nama_pengarang.append(nama_pengarang_input)
    penerbit.append(penerbit_input)
    tahun_terbit.append(tahun_terbit_input_bukan_list)
    genre_buku.append(genre_buku_input)
    jumlah_halaman.append(jumlah_halaman_input_bukan_list)
    nama_peminjam.append(nama_peminjam_input)
    yes_no()    
    menu_utama_perpustakaan()

#definition list untuk menu yes or no
def yes_no():
    list_buku()
    yes_no_confimation=input("Apakah ada data yang ingin diganti(yes/no)? ").lower()
    while True:
        if yes_no_confimation.lower()=="yes":
            menu_revision_data_buku()
            break
        elif yes_no_confimation.lower()=="no":
            menu_utama_perpustakaan()
            break
        else:
            print("Input yang dimasukkan tidak sesuai dengan petunjuk")
            continue

#Pemilihan menu yang mau diedit ulang
def menu_revision_data_buku():
    list_1_hingga_8_menu_ubah_data = [
        "1. Judul Buku",
        "2. Nama Pengarang",
        "3. Penerbit",
        "4. Tahun Terbit",
        "5. Genre Buku",
        "6. Jumlah Halaman",
        "7. Nama Peminjam",
        "8. Kembali ke menu utama"
    ]
    print("Data yang ingin diganti:")
    for i in list_1_hingga_8_menu_ubah_data:
        print(i)
    while True:
        pilihan_angka = input("Masukkan pilihan dengan angka(1-8): ")
        if pilihan_angka in ("1", "2", "3", "4", "5", "6", "7", "8"):
            pilihan_angka_int=int(pilihan_angka)
            break
        else:
            print("Input tidak sesuai dengan petunjuk. Ulangi lagi")
    while True:
        if pilihan_angka_int==1:
            menu_ganti_judul_buku()
            break
        elif pilihan_angka_int==2:
            menu_ganti_pengarang()
            break
        elif pilihan_angka_int==3:
            menu_ganti_penerbit()
            break
        elif pilihan_angka_int==4:
            menu_ganti_tahun_terbit()
            break
        elif pilihan_angka_int==5:
            menu_ganti_genre_buku()
            break
        elif pilihan_angka_int==6:
            menu_ganti_jumlah_halaman()
            break
        elif pilihan_angka_int==7:
            menu_ganti_nama_peminjam()
            break
        elif pilihan_angka_int==8:
            menu_utama_perpustakaan()
            break
        else:
            print("Input yang dimassukan Tidak sesuai dengan petunjuk")
            continue

#list definition untuk apa aja yang mau diedit ulang
def menu_ganti_judul_buku():
    global index_peminjam, judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("judul_buku")
        judul_buku_yang_mau_diubah=input("Masukkan judul buku yang hendak diubah: ").lower()
        ada_berapa_judul_buku_yang_mau_diubah=[] 
        for i in range(len(judul_buku)):
            if judul_buku[i]==judul_buku_yang_mau_diubah: 
                ada_berapa_judul_buku_yang_mau_diubah.append(i)
        
            if len(ada_berapa_judul_buku_yang_mau_diubah)==0:
                print("Buku tidak terdaftar di dalam library")
                continue

            elif len(ada_berapa_judul_buku_yang_mau_diubah)==1: 
                judul_buku_baru=input("Masukkan judul yang baru: ").lower()
                Confirmation_ganti_judul_buku=input("Apakah Anda yakin ingin mengganti data judul buku ini? (Yes/No): ").lower()
                if Confirmation_ganti_judul_buku=="yes": 
                    judul_buku_index=judul_buku.index(judul_buku_yang_mau_diubah) 
                    judul_buku[judul_buku_index]=judul_buku_baru 
                elif Confirmation_ganti_judul_buku=="no":
                    menu_menambah_buku()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")

            elif len(ada_berapa_judul_buku_yang_mau_diubah)>=2:
                print(f"{'Book ID':<12}\t|{'Judul Buku':<15}")
                for i in ada_berapa_judul_buku_yang_mau_diubah:
                    print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}")
                input_id_buku=input("Masukkan ID buku yang ingin diganti: ")
                if input_id_buku not in index_peminjam: 
                    print("ID buku salah atau tidak terdaftar di dalam library")
                    continue
                else:                
                    judul_buku_baru=input("Masukkan judul yang baru: ").lower()
                    judul_buku_baru_confirm=input("Apakah Anda yakin ingin mengganti data judul buku ini? (Yes/No): ").lower()
                    if judul_buku_baru_confirm=="yes":
                        judul_buku_index=index_peminjam.index(input_id_buku) 
                        judul_buku[judul_buku_index]=judul_buku_baru 
                    if judul_buku_baru_confirm=="no":
                        menu_revision_data_buku()
                    else:
                        print("Input yang anda masukkan tidak sesuai dengan instruksi!")   
                break           
            yes_no() 

def menu_ganti_pengarang():
    global index_peminjam, judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("nama_pengarang")
        nama_pengarang_yang_mau_diubah=input("Masukkan nama Pengarang yang hendak diubah: ").lower()
        ada_berapa_nama_pengarang_yang_mau_diubah=[] 
        for i in range(len(nama_pengarang)):
            if nama_pengarang[i]==nama_pengarang_yang_mau_diubah: 
                ada_berapa_nama_pengarang_yang_mau_diubah.append(i)
                

        while True:
            if len(ada_berapa_nama_pengarang_yang_mau_diubah)==0:
                print("Buku tidak terdaftar di dalam library")
                continue

            if len(ada_berapa_nama_pengarang_yang_mau_diubah)==1: 
                nama_pengarang_baru=input("Masukkan judul yang baru: ").lower()
                Confirmation_ganti_nama_pengarang=input("Apakah Anda yakin ingin mengganti data nama Pengarang ini? (Yes/No): ").lower()
                if Confirmation_ganti_nama_pengarang=="yes": 
                    nama_pengarang_index=nama_pengarang.index(nama_pengarang_yang_mau_diubah) 
                    nama_pengarang[nama_pengarang_index]=nama_pengarang_baru 
                elif Confirmation_ganti_nama_pengarang=="no":
                    menu_menambah_buku()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")

            elif len(ada_berapa_nama_pengarang_yang_mau_diubah)>=2: 
                print(f"{'Book ID':<12}\t|{'Nama Pengarang':<10}")
                for i in ada_berapa_nama_pengarang_yang_mau_diubah:
                    print(f"{index_peminjam[i]:<12}\t|{nama_pengarang[i]:<10}")
                input_id_buku=input("Masukkan ID buku yang ingin diganti: ")
                if input_id_buku not in index_peminjam: 
                    print("ID buku salah atau tidak terdaftar di dalam library")
                    continue
                else:                
                    nama_pengarang_baru=input("Masukkan nama Pengarang yang baru: ").lower()
                    nama_pengarang_baru_confirm=input("Apakah Anda yakin ingin mengganti data nama pengarang ini? (Yes/No): ").lower()
                    if nama_pengarang_baru_confirm=="yes":
                        nama_pengarang_index=index_peminjam.index(input_id_buku) 
                        nama_pengarang[nama_pengarang_index]=nama_pengarang_baru 
                        if nama_pengarang_baru.isalpha():
                            pass
                        else:
                            print("Input harus berupa huruf!")
                            continue
                    if nama_pengarang_baru_confirm=="no":
                        menu_revision_data_buku()
                    else:
                        print("Input yang anda masukkan tidak sesuai dengan instruksi!")   
            break           
        yes_no() 

def menu_ganti_penerbit():
    global index_peminjam, judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("penerbit")
        penerbit_yang_mau_diubah=input("Masukkan penerbit yang hendak diubah: ").lower()
        ada_berapa_penerbit_yang_mau_diubah=[] 
        for i in range(len(penerbit)):
            if penerbit[i]==penerbit_yang_mau_diubah: 
                ada_berapa_penerbit_yang_mau_diubah.append(i)
                
        while True:
            if len(ada_berapa_penerbit_yang_mau_diubah)==0:
                print("Buku tidak terdaftar di dalam library")
                continue

            if len(ada_berapa_penerbit_yang_mau_diubah)==1: 
                penerbit_baru=input("Masukkan penerbit yang baru: ").lower()
                Confirmation_ganti_penerbit=input("Apakah Anda yakin ingin mengganti data penerbit buku ini? (Yes/No): ").lower()
                if Confirmation_ganti_penerbit=="yes": 
                    penerbit_index=penerbit.index(penerbit_yang_mau_diubah) 
                    penerbit[penerbit_index]=penerbit_baru 
                elif Confirmation_ganti_penerbit=="no":
                    menu_revision_data_buku()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")

            elif len(ada_berapa_penerbit_yang_mau_diubah)>=2:
                print(f"{'Book ID':<12}\t|{'Penerbit':<10}")
                for i in ada_berapa_penerbit_yang_mau_diubah:
                    print(f"{index_peminjam[i]:<12}\t|{penerbit[i]:<10}")
                input_id_buku=input("Masukkan ID buku yang ingin diganti: ")
                if input_id_buku not in index_peminjam: 
                    print("ID buku salah atau tidak terdaftar di dalam library")
                    continue
                else:                
                    penerbit_baru=input("Masukkan penerbit yang baru: ").lower()
                    penerbit_baru_confirm=input("Apakah Anda yakin ingin mengganti data penerbit buku ini? (Yes/No): ").lower()
                    if penerbit_baru_confirm=="yes":
                        penerbit_index=penerbit.index(input_id_buku) 
                        penerbit[penerbit_index]=penerbit_baru 
                    if penerbit_baru_confirm=="no":
                        menu_menambah_buku()
                    else:
                        print("Input yang anda masukkan tidak sesuai dengan instruksi!")   
            break           
        yes_no() 

def menu_ganti_tahun_terbit():
    def tahun_terbit_baru_sama_dari_1(tahun_terbit_baru_integer=""):
        tahun_terbit_yang_mau_diubah = input("Masukkan tahun terbit yang hendak diubah: ")
        if tahun_terbit_yang_mau_diubah.isdigit():
            tahun_terbit_yang_mau_diubah_integer = int(tahun_terbit_yang_mau_diubah)
        else:
            print("Input harus berupa angka.")
        while True:
            global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
            tahun_terbit_baru_input = input("Masukkan tahun terbit yang baru: ")
            if not tahun_terbit_baru_input.isdigit():
                print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
                continue
            else:
                tahun_terbit_baru_integer=int(tahun_terbit_baru_input)

            tahun_terbit_baru_confirmation=input("Apakah anda yakin ingin mengubah tahun terbit buku(Yes/No)?").lower()
            if tahun_terbit_baru_confirmation=="yes":
                if tahun_terbit_yang_mau_diubah_integer in tahun_terbit:
                    tahun_terbit_index = tahun_terbit.index(tahun_terbit_yang_mau_diubah_integer)
                    tahun_terbit[tahun_terbit_index] = tahun_terbit_baru_integer
                    break
                else:
                    print("Tahun terbit tidak ditemukan dalam library.")
                    continue
            if tahun_terbit_baru_confirmation=="no":
                menu_revision_data_buku()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
                    
    def tahun_terbit_baru_lebih_dari_1(tahun_terbit_baru_integer=""):
        while True:
            global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
            print(f"{'Book ID':<12}\t|{'Tahun Terbit':<10}")
            for i in ada_berapa_tahun_terbit_yang_mau_diubah:
                print(f"{index_peminjam[i]:<12}\t|{tahun_terbit[i]:<10}")
            input_id_buku = input("Masukkan ID buku yang ingin diganti: ")
            if input_id_buku not in index_peminjam: 
                print("ID buku salah atau tidak terdaftar di dalam library")
                continue
            
            tahun_terbit_baru_input = input("Masukkan tahun terbit yang baru: ")
            if not tahun_terbit_baru_input.isdigit():
                print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
                continue
            else:
                tahun_terbit_baru_integer=int(tahun_terbit_baru_input)
                pass

            tahun_terbit_baru_confirmation=input("Apakah anda yakin ingin mengubah tahun terbit buku?").lower()
            if tahun_terbit_baru_confirmation=="yes":
                tahun_terbit_index = index_peminjam.index(input_id_buku)
                tahun_terbit[tahun_terbit_index] = tahun_terbit_baru_integer
            if tahun_terbit_baru_confirmation=="no":
                menu_revision_data_buku()
            else:
                print("Input yang anda masukkan tidak sesuai dengan instruksi!")

    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
   
    while True:
        tahun_terbit_yang_mau_diubah = input("Masukkan tahun terbit yang hendak diubah: ")
        if not tahun_terbit_yang_mau_diubah.isdigit():
            print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
            continue
        else:
            tahun_terbit_yang_mau_diubah_integer=int(tahun_terbit_yang_mau_diubah)
            
        ada_berapa_tahun_terbit_yang_mau_diubah = [] 
        for i in range(len(tahun_terbit)):
            if tahun_terbit[i] == tahun_terbit_yang_mau_diubah_integer:
                ada_berapa_tahun_terbit_yang_mau_diubah.append(i)

        while True:
            if len(ada_berapa_tahun_terbit_yang_mau_diubah)==0:
                print("Tahun terbit tidak terdaftar di dalam library")
                continue

            elif len(ada_berapa_tahun_terbit_yang_mau_diubah) == 1:
                tahun_terbit_baru_sama_dari_1() 
            else:
                tahun_terbit_baru_lebih_dari_1()                

            break
        yes_no()

def menu_ganti_genre_buku():
    global index_peminjam, judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("genre_buku")
        genre_buku_yang_mau_diubah=input("Masukkan genre yang hendak diubah: ").lower()
        ada_berapa_genre_buku_yang_mau_diubah=[] 
        for i in range(len(genre_buku)):
            if genre_buku[i]==genre_buku_yang_mau_diubah: 
                ada_berapa_genre_buku_yang_mau_diubah.append(i)
                

        while True:
            if len(ada_berapa_genre_buku_yang_mau_diubah)==0:
                print("Buku tidak terdaftar di dalam library")
                continue

            if len(ada_berapa_genre_buku_yang_mau_diubah)==1: 
                genre_buku_baru=input("Masukkan genre yang baru: ").lower()
                Confirmation_ganti_genre_buku=input("Apakah Anda yakin ingin mengganti data genre buku ini? (Yes/No): ").lower()
                if Confirmation_ganti_genre_buku=="yes": 
                    genre_buku_index=genre_buku.index(genre_buku_yang_mau_diubah) 
                    genre_buku[genre_buku_index]=genre_buku_baru 
                    if genre_buku_baru.isalpha():
                        pass
                    else:
                        print("Input harus berupa huruf!")
                        continue
                elif Confirmation_ganti_genre_buku=="no":
                    menu_menambah_buku()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")

            elif len(ada_berapa_genre_buku_yang_mau_diubah)>=2:
                print(f"{'Book ID':<12}\t|{'Genre Buku':<10}")
                for i in ada_berapa_genre_buku_yang_mau_diubah:
                    print(f"{index_peminjam[i]:<12}\t|{genre_buku[i]:<10}")
                input_id_buku=input("Masukkan ID buku yang ingin diganti: ")
                if input_id_buku not in index_peminjam: 
                    print("ID buku salah atau tidak terdaftar di dalam library")
                    continue
                else:                
                    genre_buku_baru=input("Masukkan genre yang baru: ").lower()
                    genre_buku_baru_confirm=input("Apakah Anda yakin ingin mengganti data genre buku ini? (Yes/No): ").lower()
                    if genre_buku_baru_confirm=="yes":
                        genre_buku_index=index_peminjam.index(input_id_buku) 
                        genre_buku[genre_buku_index]=genre_buku_baru 
                        if genre_buku_baru.isalpha():
                            pass
                        else:
                            print("Input harus berupa huruf!")
                            continue
                    if genre_buku_baru_confirm=="no":
                        menu_revision_data_buku()
                    else:
                        print("Input yang anda masukkan tidak sesuai dengan instruksi!")   
            break           
        yes_no() 

def menu_ganti_jumlah_halaman():
    def jumlah_halaman_baru_sama_dari_1(jumlah_halaman_baru_integer=""):
        jumlah_halaman_yang_mau_diubah = input("Masukkan jumlah halaman yang hendak diubah: ")
        if jumlah_halaman_yang_mau_diubah.isdigit():
            jumlah_halaman_yang_mau_diubah_integer = int(jumlah_halaman_yang_mau_diubah)
        else:
            print("Input harus berupa angka.")
        while True:
            global index_peminjam,judul_buku, nama_pengarang, penerbit, jumlah_halaman, genre_buku, nama_peminjam
            jumlah_halaman_baru_input = input("Masukkan jumlah halaman yang baru: ")
            if not jumlah_halaman_baru_input.isdigit():
                print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
                continue
            else:
                jumlah_halaman_baru_integer=int(jumlah_halaman_baru_input)

            jumlah_halaman_baru_confirmation=input("Apakah anda yakin ingin mengubah jumlah halaman buku(Yes/No)?").lower()
            if jumlah_halaman_baru_confirmation=="yes":
                if jumlah_halaman_yang_mau_diubah_integer in jumlah_halaman:
                    jumlah_halaman_index = jumlah_halaman.index(jumlah_halaman_yang_mau_diubah_integer)
                    jumlah_halaman[jumlah_halaman_index] = jumlah_halaman_baru_integer
                    break
                else:
                    print("Jumlah halaman tidak ditemukan dalam library.")
                    continue
            if jumlah_halaman_baru_confirmation=="no":
                menu_revision_data_buku()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
                    
    def jumlah_halaman_baru_lebih_dari_1(jumlah_halaman_baru_integer=""):
        while True:
            global index_peminjam,judul_buku, nama_pengarang, penerbit, jumlah_halaman, genre_buku, nama_peminjam
            print(f"{'Book ID':<12}\t|{'Jumlah halaman':<10}")
            for i in ada_berapa_jumlah_halaman_yang_mau_diubah:
                print(f"{index_peminjam[i]:<12}\t|{jumlah_halaman[i]:<10}")
            input_id_buku = input("Masukkan ID buku yang ingin diganti: ")
            if input_id_buku not in index_peminjam: 
                print("ID buku salah atau tidak terdaftar di dalam library")
                continue
            
            jumlah_halaman_baru_input = input("Masukkan jumlah halaman yang baru: ")
            if not jumlah_halaman_baru_input.isdigit():
                print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
                continue
            else:
                jumlah_halaman_baru_integer=int(jumlah_halaman_baru_input)
                pass

            jumlah_halaman_baru_confirmation=input("Apakah anda yakin ingin mengubah jumlah halaman buku?").lower()
            if jumlah_halaman_baru_confirmation=="yes":
                jumlah_halaman_index = index_peminjam.index(input_id_buku)
                jumlah_halaman[jumlah_halaman_index] = jumlah_halaman_baru_integer
            if jumlah_halaman_baru_confirmation=="no":
                menu_revision_data_buku()
            else:
                print("Input yang anda masukkan tidak sesuai dengan instruksi!")

    global index_peminjam,judul_buku, nama_pengarang, penerbit, jumlah_halaman, genre_buku, jumlah_halaman, nama_peminjam
   
    while True:
        jumlah_halaman_yang_mau_diubah = input("Masukkan jumlah halaman yang hendak diubah: ")
        if not jumlah_halaman_yang_mau_diubah.isdigit():
            print("Input yang anda Masukkan tidak sesuai dengan petunjuk")
            continue
        else:
            jumlah_halaman_yang_mau_diubah_integer=int(jumlah_halaman_yang_mau_diubah)
            
        ada_berapa_jumlah_halaman_yang_mau_diubah = [] 
        for i in range(len(jumlah_halaman)):
            if jumlah_halaman[i] == jumlah_halaman_yang_mau_diubah_integer:
                ada_berapa_jumlah_halaman_yang_mau_diubah.append(i)

        while True:
            if len(ada_berapa_jumlah_halaman_yang_mau_diubah)==0:
                print("Jumlah halaman tidak terdaftar di dalam library")
                continue

            elif len(ada_berapa_jumlah_halaman_yang_mau_diubah) == 1:
                jumlah_halaman_baru_sama_dari_1() 
            else:
                jumlah_halaman_baru_lebih_dari_1()                

            break
        yes_no()

def menu_ganti_nama_peminjam():
    global index_peminjam, judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("nama_peminjam")
        nama_peminjam_yang_mau_diubah=input("Masukkan nama peminjam yang hendak diubah: ").lower()
        ada_berapa_nama_peminjam_yang_mau_diubah=[] 
        for i in range(len(nama_peminjam)):
            if nama_peminjam[i]==nama_peminjam_yang_mau_diubah: 
                ada_berapa_nama_peminjam_yang_mau_diubah.append(i)
                

        while True:
            if len(ada_berapa_nama_peminjam_yang_mau_diubah)==0:
                print("Buku tidak terdaftar di dalam library")
                continue

            if len(ada_berapa_nama_peminjam_yang_mau_diubah)==1: 
                nama_peminjam_baru=input("Masukkan nama peminjam yang baru: ").lower()
                Confirmation_ganti_nama_peminjam=input("Apakah Anda yakin ingin mengganti data nama_peminjam buku ini? (Yes/No): ").lower()
                if Confirmation_ganti_nama_peminjam=="yes": 
                    nama_peminjam_index=nama_peminjam.index(nama_peminjam_yang_mau_diubah) 
                    nama_peminjam[nama_peminjam_index]=nama_peminjam_baru 
                    if nama_peminjam_baru.isalpha():
                        pass
                    else:
                        print("Input harus berupa huruf!")
                        continue
                elif Confirmation_ganti_nama_peminjam=="no":
                    menu_menambah_buku()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")

            elif len(ada_berapa_nama_peminjam_yang_mau_diubah)>=2: 
                print(f"{'Book ID':<12}\t|{'Nama Peminjam':<10}")
                for i in ada_berapa_nama_peminjam_yang_mau_diubah:
                    print(f"{index_peminjam[i]:<20}\t|{nama_peminjam[i]:<10}")
                input_id_buku=input("Masukkan ID buku yang ingin diganti: ")
                if input_id_buku not in index_peminjam: 
                    print("ID buku salah atau tidak terdaftar di dalam library")
                    continue
                else:                
                    nama_peminjam_baru=input("Masukkan nama peminjam yang baru: ").lower()
                    nama_peminjam_baru_confirm=input("Apakah Anda yakin ingin mengganti data nama peminjam buku ini? (Yes/No): ").lower()
                    if nama_peminjam_baru_confirm=="yes":
                        nama_peminjam_index=index_peminjam.index(input_id_buku) 
                        nama_peminjam[nama_peminjam_index]=nama_peminjam_baru 
                        if nama_peminjam_baru.isalpha():
                            pass
                        else:
                            print("Input harus berupa huruf!")
                            continue
                    if nama_peminjam_baru_confirm=="no":
                        menu_menambah_buku()
                    else:
                        print("Input yang anda masukkan tidak sesuai dengan instruksi!")   
            break           
        yes_no() 






#Menu 2
#Menu menghapus data
def menghapus_data():
    global judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        def menu_hapus_data():
            print("Masukkan pilihan cara menghapus data: ")
            print("1. Berdasarkan ID buku")
            print("2. Berdasarkan data buku")
            print("3. Kembali ke menu utama")
            hapus_data_input=input("Input angka cara menghapus data: ")
            return hapus_data_input
        menu_hapus_data_input=menu_hapus_data()
        if not menu_hapus_data_input.isdigit():
            print("Input yang dimassukan tidak sesuai dengan petunjuk")
        else:
            hapus_data_input_integer=int(menu_hapus_data_input)
            if hapus_data_input_integer==1:
                hapus_dengan_id_buku()
                break
            elif hapus_data_input_integer==2:
                menu_hapus_data_buku()
                break
            elif hapus_data_input_integer==3:
                menu_utama_perpustakaan()
                break
            else:
                print("Input yang dimassukan tidak sesuai dengan petunjuk")
                continue

#Menu Menghapus dengan data buku
def menu_hapus_data_buku():
    while True:
        print("Cara menghapus data buku:")
        print("1. Judul Buku")
        print("2. Pengarang")
        print("3. Genre")
        print("4. Kembali ke menu hapus data")
        print("5. Kembali ke menu utama")
        cara_hapus_data_buku=input("Masukkan cara menghapus data buku: ")
        if cara_hapus_data_buku=="1":
            hapus_dengan_judul_buku()
            break
        elif cara_hapus_data_buku=="2":
            hapus_dengan_pengarang()
            break
        elif cara_hapus_data_buku=="3":
            hapus_dengan_genre_buku()
            break
        elif cara_hapus_data_buku=="4":
            menghapus_data()
            break
        elif cara_hapus_data_buku=="5":
            menu_utama_perpustakaan()
            break
        else:
            print("Input yang dimassukan tidak sesuai dengan petunjuk!")
            continue

#Menghapus dengan ID buku
def hapus_dengan_id_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    list_buku()
    while True:
            id_buku_yang_dihapus_input=input("Masukkan ID buku yang ingin dihapus")
            if not id_buku_yang_dihapus_input in index_peminjam:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
            else:
                id_buku_yang_dihapus_input_index=index_peminjam.index(id_buku_yang_dihapus_input)
                
            input_pemastian=input("Apakah anda yakin ingin menghapus buku dari library(Yes/No): ")
            if input_pemastian.lower()=="yes":
                del index_peminjam[id_buku_yang_dihapus_input_index]
                del judul_buku[id_buku_yang_dihapus_input_index]
                del nama_pengarang[id_buku_yang_dihapus_input_index]
                del penerbit[id_buku_yang_dihapus_input_index]
                del tahun_terbit[id_buku_yang_dihapus_input_index]
                del genre_buku[id_buku_yang_dihapus_input_index]
                del jumlah_halaman[id_buku_yang_dihapus_input_index]
                del nama_peminjam[id_buku_yang_dihapus_input_index]
                break
            
            elif input_pemastian.lower()=="no":
                menghapus_data()
            else:
                print("Input yang anda masukkan tidak sesuai dengan petunjuk")
                continue
    print("Buku sudah berhasil terhapus")
    list_buku()
    menu_utama_perpustakaan() 

#Menu hapus data buku berdasarkan judul buku, pengarang, dan genre
def hapus_dengan_judul_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("judul_buku")
        judul_buku_yang_mau_dihapus=input("Massukan judul buku: ").lower()
        jumlah_judul_buku_yang_mau_dihapus=[]
        for i in range(len(judul_buku)):
            if judul_buku[i]==judul_buku_yang_mau_dihapus:
                jumlah_judul_buku_yang_mau_dihapus.append(i)
        
        while True:
            if len(jumlah_judul_buku_yang_mau_dihapus)==0:
                print("Judul yang dimasukkan tidak terdaftar di dalam library")
                continue

            elif len(jumlah_judul_buku_yang_mau_dihapus)==1:
                confirmation_input=input("Apakah anda yakin mau menghapus data buku ini(Yes/No): ")
                if confirmation_input=="yes":
                    judul_buku_yang_mau_dihapus_index=judul_buku.index(judul_buku_yang_mau_dihapus)
                    del index_peminjam[judul_buku_yang_mau_dihapus_index]
                    del judul_buku[judul_buku_yang_mau_dihapus_index]
                    del nama_pengarang[judul_buku_yang_mau_dihapus_index]
                    del penerbit[judul_buku_yang_mau_dihapus_index]
                    del genre_buku[judul_buku_yang_mau_dihapus_index]
                    del jumlah_halaman[judul_buku_yang_mau_dihapus_index]
                    del nama_peminjam[judul_buku_yang_mau_dihapus_index]
                    break
                elif confirmation_input=="no":
                    menghapus_data()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk!")   
            
            elif len(jumlah_judul_buku_yang_mau_dihapus)>=2:
                print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}\t|{'Penerbit':<10}\t")
                for i in jumlah_judul_buku_yang_mau_dihapus:
                    print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}\t|{penerbit[i]:<10}\t|")
                kode_id_buku_hapus=input("Masukkan kode ID buku: ")
                if kode_id_buku_hapus in index_peminjam:
                    pass
                else:
                    print("ID buku yang dimassukan tidak terdaftar di dalam library")
                    continue
                confirmation_ID=input("Apakah anda yakin ingin menghapus data buku ini(Yes/No): ").lower()
                if confirmation_ID=="yes":
                    kode_id_buku_hapus_index=index_peminjam.index(kode_id_buku_hapus)
                    del index_peminjam[kode_id_buku_hapus_index]
                    del judul_buku[kode_id_buku_hapus_index]
                    del nama_pengarang[kode_id_buku_hapus_index]
                    del penerbit[kode_id_buku_hapus_index]
                    del genre_buku[kode_id_buku_hapus_index]
                    del jumlah_halaman[kode_id_buku_hapus_index]
                    del nama_peminjam[kode_id_buku_hapus_index]
                    break
                elif confirmation_ID=="no":
                    menghapus_data()
                else:
                    print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                    continue
            
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
            break

        print("Data buku sudah terhapus dari library")
        menghapus_data()

def hapus_dengan_pengarang():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("nama_pengarang")
        nama_pengarang_yang_mau_dihapus=input("Massukan nama pengarang: ").lower()
        jumlah_nama_pengarang_yang_mau_dihapus=[]
        for i in range(len(nama_pengarang)):
            if nama_pengarang[i]==nama_pengarang_yang_mau_dihapus:
                jumlah_nama_pengarang_yang_mau_dihapus.append(i)
            else:
                pass
        
        if len(jumlah_nama_pengarang_yang_mau_dihapus)==0:
            print("Nama pengarang tidak terdaftar di dalam library")
            continue
        elif len(jumlah_nama_pengarang_yang_mau_dihapus)==1:
            confirmation_input=input("Apakah anda yakin mau menghapus data buku ini(Yes/No): ")
            if confirmation_input=="yes":
                nama_pengarang_yang_mau_dihapus_index=nama_pengarang.index(nama_pengarang_yang_mau_dihapus)
                del index_peminjam[nama_pengarang_yang_mau_dihapus_index]
                del judul_buku[nama_pengarang_yang_mau_dihapus_index]
                del nama_pengarang[nama_pengarang_yang_mau_dihapus_index]
                del penerbit[nama_pengarang_yang_mau_dihapus_index]
                del genre_buku[nama_pengarang_yang_mau_dihapus_index]
                del jumlah_halaman[nama_pengarang_yang_mau_dihapus_index]
                del nama_peminjam[nama_pengarang_yang_mau_dihapus_index]
                break
            elif confirmation_input=="no":
                menghapus_data()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk!")
                continue   
            
        elif len(jumlah_nama_pengarang_yang_mau_dihapus)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}")
            for i in jumlah_nama_pengarang_yang_mau_dihapus:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}")
            kode_id_buku_hapus=input("Masukkan kode ID buku: ")
            if kode_id_buku_hapus in index_peminjam:
                pass
            else:
                print("ID buku yang dimassukan tidak terdaftar di dalam library")
                continue
            confirmation_ID=input("Apakah anda yakin ingin menghapus data buku ini(Yes/No): ").lower()
            if confirmation_ID=="yes":
                kode_id_buku_hapus_index=index_peminjam.index(kode_id_buku_hapus)
                del index_peminjam[kode_id_buku_hapus_index]
                del judul_buku[kode_id_buku_hapus_index]
                del nama_pengarang[kode_id_buku_hapus_index]
                del penerbit[kode_id_buku_hapus_index]
                del genre_buku[kode_id_buku_hapus_index]
                del jumlah_halaman[kode_id_buku_hapus_index]
                del nama_peminjam[kode_id_buku_hapus_index]
                break
            elif confirmation_ID=="no":
                menghapus_data()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
            
        else:
            print("Input yang dimasukkan tidak sesuai dengan petunjuk")
            continue
        break
    print("Data buku sudah terhapus dari library")
    menghapus_data()                

def hapus_dengan_genre_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        list_buku("genre_buku")
        genre_buku_yang_mau_dihapus=input("Massukan genre buku yang ingin dihapus: ").lower()
        jumlah_genre_buku_yang_mau_dihapus=[]
        for i in range(len(genre_buku)):
            if genre_buku[i]==genre_buku_yang_mau_dihapus:
                jumlah_genre_buku_yang_mau_dihapus.append(i)
            else:
                pass
        
        if len(jumlah_genre_buku_yang_mau_dihapus)==0:
            print("Judul yang dimasukkan tidak terdaftar di dalam library")
            continue
            
        elif len(jumlah_genre_buku_yang_mau_dihapus)==1:
            confirmation_input=input("Apakah anda yakin mau menghapus data buku ini(Yes/No): ")
            if confirmation_input=="yes":
                genre_buku_yang_mau_dihapus_index=genre_buku.index(genre_buku_yang_mau_dihapus)
                del index_peminjam[genre_buku_yang_mau_dihapus_index]
                del judul_buku[genre_buku_yang_mau_dihapus_index]
                del nama_pengarang[genre_buku_yang_mau_dihapus_index]
                del penerbit[genre_buku_yang_mau_dihapus_index]
                del genre_buku[genre_buku_yang_mau_dihapus_index]
                del jumlah_halaman[genre_buku_yang_mau_dihapus_index]
                del nama_peminjam[genre_buku_yang_mau_dihapus_index]
                break
            elif confirmation_input=="no":
                menghapus_data()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk!")
                continue   
            
        elif len(jumlah_genre_buku_yang_mau_dihapus)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Genre Buku':<10}")
            for i in jumlah_genre_buku_yang_mau_dihapus:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{genre_buku[i]:<10}")
            kode_id_buku_hapus=input("Masukkan kode ID buku: ")
            if kode_id_buku_hapus in index_peminjam:
                pass
            else:
                print("ID buku yang dimassukan tidak terdaftar di dalam library")
                continue
            confirmation_ID=input("Apakah anda yakin ingin menghapus data buku ini(Yes/No): ").lower()
            if confirmation_ID=="yes":
                kode_id_buku_hapus_index=index_peminjam.index(kode_id_buku_hapus)
                del index_peminjam[kode_id_buku_hapus_index]
                del judul_buku[kode_id_buku_hapus_index]
                del nama_pengarang[kode_id_buku_hapus_index]
                del penerbit[kode_id_buku_hapus_index]
                del genre_buku[kode_id_buku_hapus_index]
                del jumlah_halaman[kode_id_buku_hapus_index]
                del nama_peminjam[kode_id_buku_hapus_index]
                break
            elif confirmation_ID=="no":
                menghapus_data()
            else:
                print("Input yang dimasukkan tidak sesuai dengan petunjuk")
                continue
            
        else:
            print("Input yang dimasukkan tidak sesuai dengan petunjuk")
            continue
        break
    print("Data buku sudah terhapus dari library")
    menghapus_data()                   







#Menu 3
#Menu Pencarian Buku
def menu_pencarian_buku():
    while True:
        print("Pilihan Pencarian buku: ")
        print("1. Tampilkan seluruh buku")
        print("2. Tampilkan berdasarkan data buku")
        print("3. Kembali ke menu utama")
        input_pilihan_pencarian_buku=input("Silahkan masukkan cara menampilkan buku(1-3): ")
        
        if not input_pilihan_pencarian_buku.isdigit():
            print("Input yang anda masukkan tidak sesuai dengan instruksi!")
            continue
        else:
            input_pilihan_pencarian_buku_integer=int(input_pilihan_pencarian_buku)
        
        if input_pilihan_pencarian_buku_integer==1:
            tampilkan_seluruh_buku()
        elif input_pilihan_pencarian_buku_integer==2:
            pass
        elif input_pilihan_pencarian_buku_integer==3:
            pass
        else:
            print("Input yang dimasukkan tidak sesuai dengan instruksi!")
            continue

#Menu berdasakran pilihan data
def menu_berdasarkan_pilihan_data():
    while True:
        print("Berdasarkan Pilihan Data")
        print("1. Judul Buku")
        print("2. Pengarang")
        print("3. Penerbit")
        print("4. Kembali ke menu pencarian buku")
        input_menu_berdasarkan_berdasarkan_pilihan_data=input("Silahkan masukkan nomor yang mau dipiliah: ")
        if not input_menu_berdasarkan_berdasarkan_pilihan_data.isdigit():
            print(input("Input yang dimasukkan tidak sesuai dengan instruksi!"))
        else:
            input_menu_berdasarkan_berdasarkan_pilihan_data_integer=int(input_menu_berdasarkan_berdasarkan_pilihan_data)
        
        if input_menu_berdasarkan_berdasarkan_pilihan_data_integer==1:
            tampilkan_berdasarkan_judul_buku()
        elif input_menu_berdasarkan_berdasarkan_pilihan_data_integer==2:
            tampilkan_berdasarkan_pengarang()
        elif input_menu_berdasarkan_berdasarkan_pilihan_data_integer==3:
            tampilkan_berdasarkan_penerbit()
        elif input_menu_berdasarkan_berdasarkan_pilihan_data_integer==4:
            menu_pencarian_buku()
        else:
            print("Input yang dimasukkan tidak sesuai dengan instruksi!")
            continue
        break

#Menu setelah buku selesai dipastikan
def menu_setelah_buku_selesai_dipastikan():
    while True:
        print("Apakah anda akan mencari lagi")
        print("1. Kembali ke menu utama")
        print("2. lanjutkan ke menu peminjaman")
        input_pilihan_balik_atau_lanjut=input("Input nomor yang mau dipilih: ")
        if not input_pilihan_balik_atau_lanjut.isdigit():
            print("Input yang dimasukkan tidak sesuai dengan instruksi!")
            continue
        else:
            input_pilihan_balik_atau_lanjut_integer=int(input_pilihan_balik_atau_lanjut)
        
        if input_pilihan_balik_atau_lanjut_integer==1:
            menu_utama_perpustakaan()
        elif input_pilihan_balik_atau_lanjut_integer==2:
            konfirmasi_nama_peminjam_dan_denda()
        else:
            print("Input yang dimasukkan tidak sesuai dengan instruksi!")
            continue

#Menu tampilkan berdasarkan seluruh buku
def tampilkan_seluruh_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    list_buku()
    print(f"Ditemukan {len(judul_buku)} Buku")
    for i in range(len(judul_buku)):
        print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
    menu_setelah_buku_selesai_dipastikan()


#Tampilkan berdasarkan pilihan data
def tampilkan_berdasarkan_judul_buku():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        masukkan_judul_buku_yang_dicari=input("Masukkan judul buku yang dicari: ").lower()
        ada_berapa_judul_buku_yang_dicari=[]
        for i in range(len(judul_buku)):
            if judul_buku[i]==masukkan_judul_buku_yang_dicari:
                ada_berapa_judul_buku_yang_dicari.append(i)

        if len(ada_berapa_judul_buku_yang_dicari)==0:
            print("Judul buku tidak ditemukan di library")
            list_buku()
            continue

        if len(ada_berapa_judul_buku_yang_dicari)==1:
            print(f"Ditemukan {len(ada_berapa_judul_buku_yang_dicari)} Buku")
            for i in ada_berapa_judul_buku_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
                break

        elif len(ada_berapa_judul_buku_yang_dicari)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}\t|{'Penerbit':<10}\t|{'Tahun Terbit':<10}\t|{'Genre Buku':<10}\t|Jumlah Halaman\t|{'Nama Peminjam':<10}")
            for i in ada_berapa_judul_buku_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}\t|{penerbit[i]:<10}\t|{tahun_terbit[i]:<10}\t|{genre_buku[i]:<10}\t|{jumlah_halaman[i]:<10}\t|{nama_peminjam[i]:<10}")
            print(f"Ditemukan {len(ada_berapa_judul_buku_yang_dicari)} Buku")
            for i in ada_berapa_judul_buku_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
        break
    menu_setelah_buku_selesai_dipastikan()        

def tampilkan_berdasarkan_pengarang():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        masukkan_nama_pengarang_yang_dicari=input("Masukkan pengarang yang dicari: ").lower()
        ada_berapa_nama_pengarang_yang_dicari=[]
        for i in range(len(nama_pengarang)):
            if nama_pengarang[i]==masukkan_nama_pengarang_yang_dicari:
                ada_berapa_nama_pengarang_yang_dicari.append(i)

        if len(ada_berapa_nama_pengarang_yang_dicari)==0:
            print("Pengarang buku tidak ditemukan di library")
            list_buku()
            continue

        if len(ada_berapa_nama_pengarang_yang_dicari)==1:
            print(f"Ditemukan {len(ada_berapa_nama_pengarang_yang_dicari)} Buku")
            for i in ada_berapa_nama_pengarang_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
                break

        elif len(ada_berapa_nama_pengarang_yang_dicari)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}\t|{'Penerbit':<10}\t|{'Tahun Terbit':<10}\t|{'Genre Buku':<10}\t|Jumlah Halaman\t|{'Nama Peminjam':<10}")
            for i in ada_berapa_nama_pengarang_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}\t|{penerbit[i]:<10}\t|{tahun_terbit[i]:<10}\t|{genre_buku[i]:<10}\t|{jumlah_halaman[i]:<10}\t|{nama_peminjam[i]:<10}")
            print(f"Ditemukan {len(ada_berapa_nama_pengarang_yang_dicari)} Buku")
            for i in ada_berapa_nama_pengarang_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
        break
    menu_setelah_buku_selesai_dipastikan()             

def tampilkan_berdasarkan_penerbit():
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    while True:
        masukkan_nama_penerbit_yang_dicari=input("Masukkan penerbit yang dicari: ").lower()
        ada_berapa_nama_penerbit_yang_dicari=[]
        for i in range(len(penerbit)):
            if penerbit[i]==masukkan_nama_penerbit_yang_dicari:
                ada_berapa_nama_penerbit_yang_dicari.append(i)

        if len(ada_berapa_nama_penerbit_yang_dicari)==0:
            print("Penerbit buku tidak ditemukan di library")
            list_buku()
            continue

        if len(ada_berapa_nama_penerbit_yang_dicari)==1:
            print(f"Ditemukan {len(ada_berapa_nama_penerbit_yang_dicari)} Buku")
            for i in ada_berapa_nama_penerbit_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
                break

        elif len(ada_berapa_nama_penerbit_yang_dicari)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Nama Pengarang':<10}\t|{'Penerbit':<10}\t|{'Tahun Terbit':<10}\t|{'Genre Buku':<10}\t|Jumlah Halaman\t|{'Nama Peminjam':<10}")
            for i in ada_berapa_nama_penerbit_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_pengarang[i]:<10}\t|{penerbit[i]:<10}\t|{tahun_terbit[i]:<10}\t|{genre_buku[i]:<10}\t|{jumlah_halaman[i]:<10}\t|{nama_peminjam[i]:<10}")
            print(f"Ditemukan {len(ada_berapa_nama_penerbit_yang_dicari)} Buku")
            for i in ada_berapa_nama_penerbit_yang_dicari:
                print(f"{i+1}. ({nama_pengarang[i]}), ({judul_buku[i]}) (({penerbit[i]}, {tahun_terbit[i]}))")
        break
    menu_setelah_buku_selesai_dipastikan()    
        






#Menu ke-4(Menu Peminjaman)

def konfirmasi_nama_peminjam_dan_denda():
    #Mengambil data berdasarkan nama peminjam
    global index_peminjam,judul_buku, nama_pengarang, penerbit, tahun_terbit, genre_buku, jumlah_halaman, nama_peminjam
    total_denda=0
    ada_berapa_nama_peminjam_yang_dicari=[]
    jumlah_hari_meminjam_integer=[]
    tanggal_mulai_meminjam=[]
    while True: 
        masukkan_nama_peminjam_yang_dicari=input("Masukkan nama peminjam yang dicari: ").lower()

        for i in range(len(nama_peminjam)):
            if nama_peminjam[i]==masukkan_nama_peminjam_yang_dicari:
                ada_berapa_nama_peminjam_yang_dicari.append(i)

        if len(ada_berapa_nama_peminjam_yang_dicari)==0:
            print("Peminjam buku tidak ditemukan di library")
            list_buku()
            continue

        elif len(ada_berapa_nama_peminjam_yang_dicari)==1:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Peminjam':<10}")
            for i in ada_berapa_nama_peminjam_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_peminjam[i]:<10}")

        elif len(ada_berapa_nama_peminjam_yang_dicari)>=2:
            print(f"{'Book ID':<12}\t|{'Judul Buku':<15}\t|{'Peminjam':<10}")
            for i in ada_berapa_nama_peminjam_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_peminjam[i]:<10}")

    #konfirmasi apakah data sudah benar
        input_konfirmasi_apakah_nama_peminjam_benar=input("Apakah nama peminjam dan buku yang dipinjam sudah betul(Yes/No): ").lower()
        if input_konfirmasi_apakah_nama_peminjam_benar=="yes":
            pass
        elif input_konfirmasi_apakah_nama_peminjam_benar=="no":
            continue
        else:
            print("Input yang dimasukkan tidak sesuai dengan Instruksi!")
    
    #Konfirmasi tanggal dan hari peminjaman(tabel baru)
        if len(ada_berapa_nama_peminjam_yang_dicari)==1:
            tanggal_mulai_meminjam_input=input("Masukkan tanggal peminjam mulai meminjam buku: ").lower()
            tanggal_mulai_meminjam.append(tanggal_mulai_meminjam_input)
            jumlah_hari_meminjam=input("Masukkan jumlah hari peminjam meminjam buku: ")
            if not jumlah_hari_meminjam.isdigit():
                print("Input harus berupa angka")
                continue
            else:
                jumlah_hari_meminjam_integer.append(int(jumlah_hari_meminjam))
            print(f"{'Book ID':<12}\t|{'nama_peminjam':<15}\t|{'Peminjam':<10}\t|{'Peminjam':<10}")
            for i in ada_berapa_nama_peminjam_yang_dicari:
                print(f"{index_peminjam[i]:<12}\t|{judul_buku[i]:<15}\t|{nama_peminjam[i]:<10}")
    
        elif len(ada_berapa_nama_peminjam_yang_dicari)>=2:
            for i in ada_berapa_nama_peminjam_yang_dicari:
                tanggal_mulai_meminjam_input=input("Masukkan tanggal peminjam mulai meminjam buku: ").lower()
                tanggal_mulai_meminjam.append(tanggal_mulai_meminjam_input)
                jumlah_hari_meminjam=input("Masukkan jumlah hari peminjam meminjam buku: ")
                if not jumlah_hari_meminjam.isdigit():
                    print("Input harus berupa angka")
                    continue
                else:
                    jumlah_hari_meminjam_integer.append(int(jumlah_hari_meminjam))
                print(f"{'Book ID':<12}\t|{'nama_peminjam':<15}\t|{'Peminjam':<10}\t|{'Peminjam':<10}")
                for i in ada_berapa_nama_peminjam_yang_dicari:
                    print(f"{index_peminjam[i]:<12}\t|{tanggal_mulai_meminjam[i]:<15}\t|{nama_peminjam[i]:<10}")
        
        #Konfirmasi apakah ada biaya denda atau tidak
        if len(ada_berapa_nama_peminjam_yang_dicari)==1:
            for i in ada_berapa_nama_peminjam_yang_dicari:
                if jumlah_hari_meminjam_integer[i]<=7:
                    print(f"Peminjam mengembalikan {judul_buku[i]} tepat pada waktunya")

            for i in ada_berapa_nama_peminjam_yang_dicari:
                if jumlah_hari_meminjam_integer[i]>7: 
                    biaya_denda=(jumlah_hari_meminjam_integer[i]-7)*4000
                    total_denda+=biaya_denda

            print(f"Biaya sewa buku: Rp {total_denda}")

            while True:
                input_jumlah_uang_yang_diberikan=input("Masukkan jumlah uang yang dibayar: ")
                if not input_jumlah_uang_yang_diberikan.isdigit():
                    print("Input hanya dapat berupa angka")
                    continue
                else:
                    input_jumlah_uang_yang_diberikan_integer=int(input_jumlah_uang_yang_diberikan)
                if total_denda==0:
                    break
                if input_jumlah_uang_yang_diberikan_integer>total_denda:
                    print(f"Uang kembalian: Rp. {input_jumlah_uang_yang_diberikan_integer-total_denda}")
                    break
                else:
                    print(f"Uang yang kurang: Rp. {total_denda-input_jumlah_uang_yang_diberikan_integer}")
                    continue
        
        elif len(ada_berapa_nama_peminjam_yang_dicari)>=2:
            for i in ada_berapa_nama_peminjam_yang_dicari:
                if jumlah_hari_meminjam_integer[i]<=7:
                    print(f"Peminjam mengembalikan {judul_buku[i]} tepat pada waktunya")

            for i in ada_berapa_nama_peminjam_yang_dicari:
                if jumlah_hari_meminjam_integer[i]>7: 
                    biaya_denda=(jumlah_hari_meminjam_integer[i]-7)*4000
                    total_denda+=biaya_denda

            print(f"Biaya sewa buku: Rp {total_denda}")

            while True:
                input_jumlah_uang_yang_diberikan=input("Masukkan jumlah uang yang dibayar: ")
                if not input_jumlah_uang_yang_diberikan.isdigit():
                    print("Input hanya dapat berupa angka")
                    continue
                else:
                    input_jumlah_uang_yang_diberikan_integer=int(input_jumlah_uang_yang_diberikan)

                if total_denda==0:
                    break
                elif input_jumlah_uang_yang_diberikan_integer>total_denda:
                    print(f"Uang kembalian: Rp.{input_jumlah_uang_yang_diberikan_integer-total_denda}")
                    break
                else:
                    print(f"Uang yang kurang: Rp.{total_denda-input_jumlah_uang_yang_diberikan_integer}")
                    continue
                
        #Menu hapus buku berdasarkan data peminjam
        for i in sorted(ada_berapa_nama_peminjam_yang_dicari,reverse=True):
            del index_peminjam[i]
            del judul_buku[i]
            del nama_pengarang[i]
            del penerbit[i]
            del genre_buku[i]
            del jumlah_halaman[i]
            del nama_peminjam[i]
        print("Buku sudah Dikembalikan")
        list_buku()
        menu_utama_perpustakaan()
                    
login()
menu_utama_perpustakaan()
            
        










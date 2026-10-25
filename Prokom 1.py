Jumlah_Pekerja = 22
pekerja_bolos = int(input("Berapa yang bolos?"))
Jumlah_Pekerja_Masuk = Jumlah_Pekerja-pekerja_bolos
print ("pekerja yang masuk:" , Jumlah_Pekerja_Masuk) 

Alas = float(input("Berapa Alasnya?"))
Tinggi = float(input("Berapa Tingginya?"))
Luas = Alas * Tinggi / 2
print("Luasnya Adalah" , Luas)

berat_std_shuttlecock_min = 5.8 #gram
berat_std_shuttlecock_maks = 6.8 #gram

Berat = float(input("berapa berat shutlecocknya?"))

if Berat <= berat_std_shuttlecock_min:
    print("tidak lolos QC")
elif Berat >= berat_std_shuttlecock_maks:
    print("tidak lolos QC")
else:
    print("lolos QC")

    
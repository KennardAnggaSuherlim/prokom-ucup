Kapasitas_Buffer = 100 ; Batas_Minimum = 50 ; Persediaan_Awal = 12 ; Jumlah_pengisian = 0 ; isi = [8,10,12,14,9,0,20]

while Persediaan_Awal <= Batas_Minimum:
    Persediaan_Awal= Persediaan_Awal + isi[Jumlah_pengisian]
    Jumlah_pengisian= Jumlah_pengisian + 1
    print ("Jumlah persediaan", Persediaan_Awal, "unit")
    print ("diisi", isi[Jumlah_pengisian])
    print ("Setelah", Jumlah_pengisian, "kali")
    
    
print ("Jumlah persediaan", Persediaan_Awal, "unit")
print ("Setelah pengisian", Jumlah_pengisian, "kali")

        
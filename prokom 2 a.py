#Deklarasi Variabel
N = 5 ; i = 1 ; TotalCacat = 0 ; JumlahBaik = 0

#blok input data
for i in range(N): # for buat looping, i mulai dari berapanya, N berapa kali looping

#input diameter cock
    Diameter_Cock = float(input("Data dieameter cock?"))
    
#keputusan
    if Diameter_Cock >= 5.8 and Diameter_Cock <= 6.8: 
        JumlahBaik = JumlahBaik + 1
        print ("Produk Baik")
        print ("Jumlah cock baik:", JumlahBaik, "buah")
        print ("====================================================================")
    else: 
        TotalCacat = TotalCacat + 1
        print ("Produk Buruk")
        print ("Jumlah cock buruk:", TotalCacat, "buah")
        print ("====================================================================")
        
PersentaseCacat = TotalCacat/N * 100
print ("====================================================================")

#ouput
print ("Jumlah Cock Baik:", JumlahBaik, "buah")
print ("Jumlah Cock Buruk:",TotalCacat, "buah")
print ("Persentase Cacat:", PersentaseCacat, "%")
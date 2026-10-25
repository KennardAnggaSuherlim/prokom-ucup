angka = []

n = int(input("Berapa banyak bilangan yang ingin dimasukkan? "))
for i in range(n):
    nilai = float(input(f"Bilangan ke-{i+1}: "))
    angka.append(nilai)

# Total (tanpa sum())
total = 0
for x in angka:
    total += x

# Rata-rata (tanpa mean())
rata = total / len(angka)

# Standar deviasi populasi (tanpa stdev())
jumlah_kuadrat = 0
for x in angka:
    jumlah_kuadrat += (x - rata) ** 2
std = (jumlah_kuadrat / len(angka)) ** 0.5

# Minimum dan maksimum (tanpa min()/max())
minimum = angka[0]
maksimum = angka[0]
for x in angka:
    if x < minimum:
        minimum = x
    if x > maksimum:
        maksimum = x

print("\nData      :", angka)
print("Total     :", total)
print("Rata-rata :", round(rata, 2))
print("Std Dev   :", round(std, 2))
print("Minimum   :", minimum)
print("Maksimum  :", maksimum)
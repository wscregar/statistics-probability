print("Wira Samudra Siregar\n5027231041\nKelas A\n")

data={100.5, 99.7, 101, 101.3, 99.9, 98.9, 165, 102.2, 98.7, 102.9, 100}
data_2={95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75}

print("(MEAN SOAL 1)\n")
print(f"DATA: {data}")

total_data_mean= sum(data)
print(f"Total Data: {sum(data)}")

jumlah_data_mean= len(data)
print(f"Jumlah Data: {len(data)}")

rata_2= total_data_mean/jumlah_data_mean
print(f"MEAN: {rata_2}\n")

print("(MEAN SOAL 2)\n")
print(f"DATA: {data_2}")

total_data_mean= sum(data_2)
print(f"Total Data: {sum(data_2)}")

jumlah_data_mean= len(data_2)
print(f"Jumlah Data: {len(data_2)}")

rata_soal_2= total_data_mean/jumlah_data_mean
print(f"MEAN: {rata_soal_2}")

print("===============================================================")

print('(MEDIAN SOAL 1)\n')

urutan_data= sorted(data)
print(f"Urutan Data: {sorted(data)}")

total_data_median= len(data)
print(f"Total Data: {len(data)}")

index_tengah= total_data_median//2

if(total_data_median % 2 == 0):
    print("Mendian Genap")
    hasil_median1= urutan_data[index_tengah]
    hasil_median2= urutan_data[index_tengah - 1]
    print(f"Nilai Tengah: {hasil_median1} {hasil_median2}")
    nilai_median= (hasil_median1+hasil_median2) / 2

else:
    print("Median Ganjil")
    nilai_median= urutan_data[index_tengah]
    print(f"Nilai tengah: {nilai_median}")

print(f"Median: {nilai_median}\n")

print("(MEDIAN SOAL 2)\n")

urutan_data= sorted(data_2)
print(f"Urutan Data: {sorted(data_2)}")

total_data_median= len(data_2)
print(f"Total Data: {len(data_2)}")

index_tengah= total_data_median//2

if(total_data_median % 2 == 0):
    print("Mendian Genap")
    hasil_median1= urutan_data[index_tengah]
    hasil_median2= urutan_data[index_tengah - 1]
    print(f"Nilai Tengah: {hasil_median1} {hasil_median2}")
    nilai_median_2= (hasil_median1+hasil_median2) / 2

else:
    print("Median Ganjil")
    nilai_median_2= urutan_data[index_tengah]
    print(f"Nilai tengah: {nilai_median_2}")

print(f"Median: {nilai_median_2}")

print("===============================================================")

from collections import Counter

print("(MODUS SOAL 1)\n")

print(f"Data: {data}")
counter = Counter(data)
mode_data = dict(counter)
muncul_terbanyak = max(list(counter.values()))
print(f"Max Counter: {muncul_terbanyak}")

mode_value = []
for k, v in mode_data.items():
    print(f"{k} muncul {v} kali")
    if v == max(list(counter.values())):
        mode_value.append(k)

print(f"Mode: {mode_value}\n")

print("(MODUS SOAL 2)\n")

print(f"Data: {data_2}")
counter = Counter(data_2)
mode_data = dict(counter)
muncul_terbanyak = max(list(counter.values()))
print(f"Max Counter: {muncul_terbanyak}")

mode_value = []
for k, v in mode_data.items():
    print(f"{k} muncul {v} kali")
    if v == max(list(counter.values())):
        mode_value.append(k)

print(f"Mode: {mode_value}")


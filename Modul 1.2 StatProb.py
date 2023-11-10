print("Wira Samudra Siregar\n5027231041\nKelas A\n")

def range(data):
    nilai_tinggi= max(data)
    print(f"Nilai Tertinggi: {max(data)}")

    nilai_rendah= min(data)
    print(f"Nilai Terendah: {min(data)}")

    range_hasil= nilai_tinggi - nilai_rendah

    print("\n")
    print(f"Range: {nilai_tinggi} - {nilai_rendah} = {range_hasil}")

    return range_hasil

print("(RANGE SOAL 1)\n")
data={19, 10, 10, 12, 13, 15, 14, 13, 9, 17}

print(f"Range: {data}")
range_hasil=range(data)

print("\n")

print("(RANGE SOAL 2)\n")
data_2={180, 185, 175, 190, 170, 195, 165 }

print(f"Range: {data_2}\n")
range_hasil=range(data_2)

print("=================================================")

print("(VARIAN SOAL 1)\n")
import statistics

print(f"Data: {data}")

rata_2= statistics.mean(data)
print(f"Mean: {rata_2}")

def varian(data):

    print(f"Hasil Kuadrat:")
squared_diff = []
for x in data:
    squared_diff_per_x = (x - rata_2) ** 2
    squared_diff.append(squared_diff_per_x)
    print(f"({x} - {rata_2})**2 = {(x - rata_2)}**2 = {squared_diff_per_x}")

print(f"Total kuadrat selisih: {sum(squared_diff)}")
print(f"Jumlah total data: {len(data)}")

varian = sum(squared_diff) / len(data)

print(f"\n")
print(f"Variansi: {sum(squared_diff)} / {len(data)} = {varian}\n")

print("(VARIAN SOAL 2)\n")
import statistics

print(f"Data: {data_2}")

rata_2= statistics.mean(data_2)
print(f"Mean: {rata_2}")

def varian(data_2):

    print(f"Hasil Kuadrat:")
squared_diff = []
for x in data_2:
    squared_diff_per_x = (x - rata_2) ** 2
    squared_diff.append(squared_diff_per_x)
    print(f"({x} - {rata_2})**2 = {(x - rata_2)}**2 = {squared_diff_per_x}")

print(f"Total kuadrat selisih: {sum(squared_diff)}")
print(f"Jumlah total data: {len(data_2)}")

varian = sum(squared_diff) / len(data_2)

print(f"\n")
print(f"Variansi: {sum(squared_diff)} / {len(data_2)} = {varian}")

print("================================================")

print("(STANDAR DEVIASI SOAL 1)\n")

print(f"Data: {data}")
rata_2= statistics.mean(data)
print(f"Mean: {rata_2}")

def varian(data):

    print(f"Hasil Kuadrat:")
squared_diff = []
for x in data:
    squared_diff_per_x = (x - rata_2) ** 2
    squared_diff.append(squared_diff_per_x)
    print(f"({x} - {rata_2})**2 = {(x - rata_2)}**2 = {squared_diff_per_x}")

print(f"Total kuadrat selisih: {sum(squared_diff)}")
print(f"Jumlah total data: {len(data)}")

varian = sum(squared_diff) / len(data)

print(f"\n")
print(f"Variansi: {sum(squared_diff)} / {len(data)} = {varian}")

standar_deviasi= varian**0.5
print(f"Standar Deviasi: {varian} ^ 0.5 = {standar_deviasi}\n")

print("(STANDAR DEVIASI SOAL 2)\n")

print(f"Data: {data_2}")
rata_2= statistics.mean(data_2)
print(f"Mean: {rata_2}")

def varian(data_2):

    print(f"Hasil Kuadrat:")
squared_diff = []
for x in data_2:
    squared_diff_per_x = (x - rata_2) ** 2
    squared_diff.append(squared_diff_per_x)
    print(f"({x} - {rata_2})**2 = {(x - rata_2)}**2 = {squared_diff_per_x}")

print(f"Total kuadrat selisih: {sum(squared_diff)}")
print(f"Jumlah total data: {len(data_2)}")

varian = sum(squared_diff) / len(data_2)

print(f"\n")
print(f"Variansi: {sum(squared_diff)} / {len(data_2)} = {varian}")

standar_deviasi= varian**0.5
print(f"Standar Deviasi: {varian} ^ 0.5 = {standar_deviasi}")






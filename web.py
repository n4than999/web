import math

print("##  Program Kalkulator Arus Bolak-Balik  ##")
print("===========================================")
print("""
1. Tegangan Melalui Resistor
2. Arus Melalui Resistor
3. Tegangan Melalui Induktor
4. Arus Melalui Induktor
5. Tegangan Melalui Kapasitor
6. Arus Melalui Kapasitor
7. Impendansi rangkaian R-L
8. Impendansi rangkaian R-C
9. Impendansi rangkaian R-L-C
10. Keluar
""")

pilihan = int(input("Input pilihan operasi: "))

if pilihan == 1:
    I = float(input("Masukkan arus (I) dalam A: "))
    R = float(input("Masukkan hambatan (R) dalam ohm: "))
    V = I * R
    print(f"\nTegangan pada resistor: V = I × R = {I} × {R} = {V:.2f} V")

elif pilihan == 2:
    V = float(input("Masukkan tegangan (V) dalam V: "))
    R = float(input("Masukkan hambatan (R) dalam ohm: "))
    I = V / R
    print(f"\nArus melalui resistor: I = V / R = {V} / {R} = {I:.2f} A")

elif pilihan == 3:
    I = float(input("Masukkan arus (I) dalam A: "))
    L = float(input("Masukkan induktansi (L) dalam H: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    V = 2 * math.pi * f * L * I
    print(f"\nTegangan pada induktor: V = 2πfLI = 2π×{f}×{L}×{I} = {V:.2f} V")

elif pilihan == 4:
    V = float(input("Masukkan tegangan (V) dalam V: "))
    L = float(input("Masukkan induktansi (L) dalam H: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    I = V / (2 * math.pi * f * L)
    print(f"\nArus melalui induktor: I = V / (2πfL) = {V} / (2π×{f}×{L}) = {I:.2f} A")

elif pilihan == 5:
    I = float(input("Masukkan arus (I) dalam A: "))
    C = float(input("Masukkan kapasitansi (C) dalam F: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    V = I / (2 * math.pi * f * C)
    print(f"\nTegangan pada kapasitor: V = I / (2πfC) = {I} / (2π×{f}×{C}) = {V:.2f} V")

elif pilihan == 6:
    V = float(input("Masukkan tegangan (V) dalam V: "))
    C = float(input("Masukkan kapasitansi (C) dalam F: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    I = V * 2 * math.pi * f * C
    print(f"\nArus melalui kapasitor: I = V × 2πfC = {V} × 2π×{f}×{C} = {I:.2f} A")

elif pilihan == 7:
    R = float(input("Masukkan hambatan (R) dalam ohm: "))
    L = float(input("Masukkan induktansi (L) dalam H: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    Z = math.sqrt(R**2 + (2 * math.pi * f * L)**2)
    print(f"\nImpedansi pada rangkaian R-L: Z = √(R² + (2πfL)²) = {Z:.2f} ohm")

elif pilihan == 8:
    R = float(input("Masukkan hambatan (R) dalam ohm: "))
    C = float(input("Masukkan kapasitansi (C) dalam F: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    Z = math.sqrt(R**2 + (1 / (2 * math.pi * f * C))**2)
    print(f"\nImpedansi pada rangkaian R-C: Z = √(R² + (1/2πfC)²) = {Z:.2f} ohm")

elif pilihan == 9:
    R = float(input("Masukkan hambatan (R) dalam ohm: "))
    L = float(input("Masukkan induktansi (L) dalam H: "))
    C = float(input("Masukkan kapasitansi (C) dalam F: "))
    f = float(input("Masukkan frekuensi (f) dalam Hz: "))
    X_L = 2 * math.pi * f * L
    X_C = 1 / (2 * math.pi * f * C)
    Z = math.sqrt(R**2 + (X_L - X_C)**2)
    print(f"\nImpedansi pada rangkaian R-L-C: Z = √(R² + (X_L - X_C)²) = {Z:.2f} ohm")

elif pilihan == 10:
    print("Program keluar")

else:
    print("Pilihan tidak valid.")

import matplotlib.pyplot as plt
import numpy as np

# Constants
Gt = Gr = 1.6  # Zyski anten
c = 3e8  # Prędkość światła (m/s)
f1 = 900e6  # Częstotliwość 1 w Hz (900 MHz)
f2 = 2400e6  # Częstotliwość 2 w Hz (2400 MHz)
lambda1 = c / f1  # Długość fali dla f1
lambda2 = c / f2  # Długość fali dla f2

# Definiowanie odległości dla części a (1 - 100 m, co 0.25 m)
distances_a = np.arange(1, 100.25, 0.25)
# Definiowanie odległości dla części b (1 m - 10 km, skala logarytmiczna)
distances_b = np.logspace(0, 4, num=1000)

# Funkcja obliczająca spadek mocy sygnału w dB
def path_loss(Gt, Gr, lambda_, d):
    return 10 * np.log10((Gt * Gr * (lambda_ / (4 * np.pi * d))**2))

# Obliczanie spadku mocy dla obu częstotliwości i obu zakresów odległości
path_loss_f1_a = path_loss(Gt, Gr, lambda1, distances_a)
path_loss_f2_a = path_loss(Gt, Gr, lambda2, distances_a)

path_loss_f1_b = path_loss(Gt, Gr, lambda1, distances_b)
path_loss_f2_b = path_loss(Gt, Gr, lambda2, distances_b)

# Wykresy dla Zadania 1 (Spadek mocy sygnału)
plt.figure(figsize=(12, 6))

# Część a: Wykres dla odległości 1-100m
plt.subplot(1, 2, 1)
plt.plot(distances_a, path_loss_f1_a, label='f1 = 900 MHz')
plt.plot(distances_a, path_loss_f2_a, label='f2 = 2400 MHz')
plt.title('Spadek mocy sygnału (1m do 100m)')
plt.xlabel('Odległość (m)')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)

# Część b: Wykres dla odległości 1m do 10km
plt.subplot(1, 2, 2)
plt.plot(distances_b / 1000, path_loss_f1_b, label='f1 = 900 MHz')
plt.plot(distances_b / 1000, path_loss_f2_b, label='f2 = 2400 MHz')
plt.title('Spadek mocy sygnału (1m do 10km)')
plt.xlabel('Odległość (km)')
plt.xscale('log')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Zadanie 2: Obliczanie opóźnień sygnału

# Obliczanie opóźnień dla odległości w części a (1-100m) i części b (1m-10km)
delay_a = distances_a / c  # Opóźnienia w sekundach dla części a
delay_b = distances_b / c  # Opóźnienia w sekundach dla części b

# Wykresy dla opóźnień sygnału (Zadanie 2)
plt.figure(figsize=(12, 6))

# Część a: Opóźnienie sygnału dla odległości 1-100m
plt.subplot(1, 2, 1)
plt.plot(distances_a, delay_a * 1e9)  # Konwersja opóźnień na nanosekundy (ns)
plt.title('Opóźnienie sygnału (1m do 100m)')
plt.xlabel('Odległość (m)')
plt.ylabel('Opóźnienie (ns)')
plt.grid(True)

# Część b: Opóźnienie sygnału dla odległości 1m do 10km
plt.subplot(1, 2, 2)
plt.plot(distances_b / 1000, delay_b * 1e9)  # Konwersja opóźnień na nanosekundy (ns)
plt.title('Opóźnienie sygnału (1m do 10km)')
plt.xlabel('Odległość (km)')
plt.xscale('log')
plt.ylabel('Opóźnienie (ns)')
plt.grid(True)

plt.tight_layout()
plt.show()
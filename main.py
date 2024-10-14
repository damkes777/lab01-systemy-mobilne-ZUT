import numpy as np
import matplotlib.pyplot as plt


def loss(gt, gr, lambda_, d):
    return 10 * np.log10((gt * gr * (lambda_ / (4 * np.pi * d)) ** 2))


gt = 1.6
gr = 1.6
c = 3e8
f1 = 900e6
f2 = 2400e6
lambda1 = c / f1
lambda2 = c / f2

distances_1 = np.arange(1, 100.25, 0.25)
distances_2 = np.arange(1, 10001, 1)

loss_1_a = loss(gt, gr, lambda1, distances_1)
loss_2_a = loss(gt, gr, lambda2, distances_1)

loss_1_b = loss(gt, gr, lambda1, distances_2)
loss_2_b = loss(gt, gr, lambda2, distances_2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(distances_1, loss_1_a, label='900 MHz')
plt.plot(distances_1, loss_2_a, label='2400 MHz')
plt.title('Spadek mocy 1m do 100m')
plt.xlabel('Odległość (m)')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(distances_2, loss_1_b, label='900 MHz')
plt.plot(distances_2, loss_2_b, label='2400 MHz')
plt.title('Spadek mocy 1m do 10km')
plt.xlabel('Odległość (m)')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('zadanie1.png')
plt.show()

delay_a = distances_1 / c
delay_b = distances_2 / c

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(distances_1, delay_a)
plt.title('Opóźnienie sygnału 1m do 100m')
plt.xlabel('Odległość (m)')
plt.ylabel('Opóźnienie (s)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(distances_2, delay_b)
plt.title('Opóźnienie sygnału 1m do 10km')
plt.xlabel('Odległość (m)')
plt.ylabel('Opóźnienie (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig('zadanie2.png')
plt.show()


Gt = 1.6
Gr = 1.6
c = 3e8
f1 = 900e6
f2 = 2400e6
lambda1 = c / f1
lambda2 = c / f2
h1 = 30
h2 = 3


def calculate_d1_d2(h1, h2, d):
    d1 = np.sqrt((h1 - h2)**2 + d**2)
    d2 = np.sqrt((h1 + h2)**2 + d**2)
    return d1, d2


def multipath_path_loss(Gt, Gr, lambda_, d1, d2, f):
    phi1 = -2 * np.pi * f * d1 / c
    phi2 = -2 * np.pi * f * d2 / c
    return 10 * np.log10(Gt * Gr * (lambda_ / (4 * np.pi))**2 * (1/d1 * np.abs(np.exp(1j * phi1)) - 1/d2 * np.abs(np.exp(1j * phi2)))**2)


distances_1 = np.arange(1, 100.25, 0.25)
distances_2 = np.arange(1, 10001, 1)

loss_1_a = []
loss_2_a = []
loss_1_b = []
loss_2_b = []

for d in distances_1:
    d1, d2 = calculate_d1_d2(h1, h2, d)
    loss_1_a.append(multipath_path_loss(Gt, Gr, lambda1, d1, d2, f1))
    loss_2_a.append(multipath_path_loss(Gt, Gr, lambda2, d1, d2, f2))

for d in distances_2:
    d1, d2 = calculate_d1_d2(h1, h2, d)
    loss_1_b.append(multipath_path_loss(Gt, Gr, lambda1, d1, d2, f1))
    loss_2_b.append(multipath_path_loss(Gt, Gr, lambda2, d1, d2, f2))

loss_1_a = np.array(loss_1_a)
loss_2_a = np.array(loss_2_a)
loss_1_b = np.array(loss_1_b)
loss_2_b = np.array(loss_2_b)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(distances_1, loss_1_a, label='900 MHz')
plt.plot(distances_1, loss_2_a, label='2400 MHz')
plt.title('Spadek mocy sygnału (1m do 100m)')
plt.xlabel('Odległość (m)')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(distances_2, loss_1_b, label='900 MHz')
plt.plot(distances_2, loss_2_b, label='2400 MHz')
plt.title('Spadek mocy sygnału (1m do 10km)')
plt.xlabel('Odległość (km)')
plt.ylabel('Spadek mocy (dB)')
plt.legend()
plt.grid(True)
plt.savefig('zadanie3.png')
plt.tight_layout()
plt.show()

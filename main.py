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
distances_2 = np.logspace(0, 4, num=1000)

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
plt.plot(distances_2 / 1000, loss_1_b, label='900 MHz')
plt.plot(distances_2 / 1000, loss_2_b, label='2400 MHz')
plt.title('Spadek mocy 1m do 10km')
plt.xlabel('Odległość (km)')
plt.xscale('log')
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
plt.xscale('log')
plt.ylabel('Opóźnienie (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig('zadanie2.png')
plt.show()

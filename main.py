import math
import matplotlib.pyplot as plt
import numpy as np

phase = 0
frequency = 100  # main harmonic frequency
sample_rate = 96000
oversampling = 32
t0 = 0
t1 = 1
dt = 1 / sample_rate
buf = 0

# cutoff simulates low pass filter with cutoff frequency = 10kHz and 6dB slope
cutoff = 0.0175 # oversampling = 32
# cutoff = 0.032 # oversampling = 16
# cutoff = 0.067 # oversampling = 8
y = []
y_raw = []
s = 0
while t0 < t1:
    phase += frequency * dt
    if phase >= 1.0:
        phase -= 1.0
    for i in range(oversampling):
        s += phase
        if s >= 1.0:
            s -= 1
            y_raw.append(1)
        else:
            y_raw.append(-1)
        buf += cutoff * (y_raw[-1] - buf)
        y.append(buf)
    t0 += dt

print(np.max(y))
plt.plot(y)
plt.show()

a = np.abs(np.fft.fftshift(np.fft.fft(y)))
b = np.fft.fftshift(np.fft.fftfreq(len(a), dt / oversampling))
a = np.divide(a, np.max(a))
plt.plot(b, a)
plt.xlim(-1, 30000)
plt.show()
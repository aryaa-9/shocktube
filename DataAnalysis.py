import numpy as np
from scipy.fft import fftfreq
from ReadingData import reads
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fft2, ifft2

def plotting(xvals, yvals, title, colors, axes):
    plt.plot(xvals, yvals, linewidth=1, color=colors)
    plt.xlabel(axes[0])
    plt.ylabel(axes[1])
    plt.title(title + ' ')
    plt.show()
    
#Discrete Fourier Transform ($ν$ (cm$^{-1}$))
def fftransform(t, ch1s, ch2s):
    N=len(t) #Total = 12500
    dt=np.diff(t)[0] #Resolution = 8.00E-09
    
    f = fftfreq(N, dt)
    ch1_FFT = fft(ch1s)
    ch2_FFT = fft(ch2s)
    
    #first half of the spectrum (real, positive values)
    plotting(f[:N//2], np.abs(ch1_FFT[:N//2]), 'frequency spectrum', 'red', ['$f_n$ [$s^{-1}$]', '|$\hat{x}_n$|'])
    plotting(f[:N//2], np.abs(ch2_FFT[:N//2]), 'frequency spectrum', 'blue', ['$f_n$ [$s^{-1}$]', '|$\hat{x}_n$|'])
    
def main():
    arrays=reads()
    HUnit, ch1s, ch2s = np.array(arrays["H_Unit"]), np.array(arrays["CH1_s"]), np.array(arrays["CH2_s"])

    plotting(HUnit, ch1s, 'Voltage vs Time (CH1)', 'lightseagreen', ['Time [s]', 'Voltage [V]'])
    plotting(HUnit, ch2s, 'Voltage vs Time (CH2)', 'pink', ['Time [s]', 'Voltage [V]'])
    fftransform(HUnit, ch1s, ch2s)
main()

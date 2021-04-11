"""
    [Feature computation library]
        With useful functions developed for the Project

    - Part of my Bachelor Thesis Project @ UC3M

    - Author: Andrea Ziqing Gallardo Bendito
    - GitHub Repo: <https://github.com/andrezg98/MusicSourceSep>
"""

# Imports
import numpy as np
import librosa
import torch


# Computing the Short Time Fourier Transform (STFT)
def __init__(self, ttype='fft', bins=48, fft_size=1024, hop_length=256, sample_rate=48000):
    self.ttype = ttype
    self.bins = bins
    self.fft_size = fft_size
    self.hop_length = hop_length
    self.sample_rate = sample_rate


# STFT of a single signal
def compute_stft(self, audio):
    audio_stft = torch.stft(audio, n_fft=float(self.fft_size), hop_length=float(self.hop_length), win_length=None,
                            window=torch.hann_window(), return_complex=True)
    mag_spec = np.abs(audio_stft)
    mag_spec_norm = mag_spec / np.sqrt(self.fft_size)  # Normalization
    return mag_spec_norm


def compute_istft(self, mag_spec_norm):
    mag_spec_istft = torch.istft(mag_spec_norm, n_fft=float(self.fft_size), hop_length=float(self.hop_length), 
                            win_length=None, window=torch.hann_window(), dtype=self.ttpye)
    return mag_spec_istft


# STFT of a matrix of signals
def compute_stft_matrix(self, audio):
    for i in range(audio.shape[1]):
        mag_spec = self.compute_stft(audio[:, i])
        if i == 0:
            mags_specs = np.zeros((audio.shape[1], mag_spec[0], mag_spec[1]))
            mags_specs[i] = mags_specs
            return mags_specs


if __name__ == "__main__":
    print("prueba 2")
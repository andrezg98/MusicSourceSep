"""
    [URMP Dataset library]
        With useful functions to extract features from
        the URMP Dataset for the Project

    - Part of my Bachelor Thesis Project @ UC3M

    - Author: Andrea Ziqing Gallardo Bendito
    - GitHub Repo: <https://github.com/andrezg98/MusicSourceSep>
"""

# Imports
import numpy as np
# import torch

# Data Extraction and Features
instruments_def = {'mix': 0, 'bn': 1, 'vc': 2, 'cl': 3, 'db': 4, 'fl': 5, 'hn': 6, 'ob': 7, 'sax': 8, 'tbn': 9,
                   'tpt': 10, 'tba': 11, 'va': 12, 'vn': 13}


class URMP(torch.utils.data.Dataset):
    def __init__(self):
        self.segment_len = 256
        self.n_orig_freq = 512
        self.n_log_sample = 256
        self.n_channels = 2  # amplitude and phase
        self.sr = 11025
        self.n_instruments = 13
        self.load_specs = True


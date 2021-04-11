"""
    [URMP Dataset Parser]
        With useful functions to extract features from
        the URMP Dataset for the Project

    - Part of my Bachelor Thesis Project @ UC3M

    - Author: Andrea Ziqing Gallardo Bendito
    - GitHub Repo: <https://github.com/andrezg98/MusicSourceSep>
"""

# Imports
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

from pathlib import Path

# Data Loading
instruments_list = {'mix': 0, 'bn': 1, 'vc': 2, 'cl': 3, 'db': 4, 'fl': 5, 'hn': 6, 'ob': 7, 'sax': 8, 'tbn': 9,
                   'tpt': 10, 'tba': 11, 'va': 12, 'vn': 13}

# Get data from filename
def get_audiofile_from_filename(filename: str):
    dir = Path(filename).dir
    if dir.startswith('AuSep'):
        instrument = dir.split('_')[2] # Example filename: AuSep_1_vn_01_Jupiter.wav
        return instruments_list[instrument]
    elif dir.startswith('AuMix'):
        return 0
    else:
        print(filename)
        raise IndexError


class URMP(Dataset):
    # URMP Dataset
    def __init__(self):
        self.segment_len = 256
        self.n_orig_freq = 512
        self.n_log_sample = 256
        self.n_channels = 2  # amplitude and phase
        self.sr = 11025
        self.n_instruments = 13
        self.load_specs = True

    def __len__(self):
        pass
    
    def __getitem__(self, metadata): # load audio files
        data = defaultdict(dict)
        for piece, filenames in list(metadata.items()):
            for filename in filenames:
                audiofile = get_audiofile_from_filename(filename) # get the number of the instrument
                data[piece][str(audiofile)] = np.load(filename)
            for key in set(str(value) for value in instruments_list.values()) - data[piece].keys():
                data[piece][key] = np.zeros(data[piece_name]['0'].shape)
        return data

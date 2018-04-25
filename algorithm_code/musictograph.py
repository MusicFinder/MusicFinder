# coding: utf-8

import librosa
import librosa.display
import glob
import matplotlib.pyplot as plt
import numpy as np
import os

base_path='MusicDatabase/'
path= glob.glob(base_path + '*.wav')
# print(len(path))

document=[os.path.basename(file_p) for file_p in path]
# print((document[0])[:-4]+'.png')
# print(path)


for index in range(len(path)):
    y, sr = librosa.load(path[index])
    # print(y)
    # print(sr)
    # print(librosa.feature.melspectrogram(y=y, sr=sr))

    # array([[  2.891e-07,   2.548e-03, ...,   8.116e-09,   5.633e-09],
    # [  1.986e-07,   1.162e-02, ...,   9.332e-08,   6.716e-09],
    # ...,
    # [  3.668e-09,   2.029e-08, ...,   3.208e-09,   2.864e-09],
    # [  2.561e-10,   2.096e-09, ...,   7.543e-10,   6.101e-10]])

    # Using a pre-computed power spectrogram
    # print(len(y), sr)
    D = np.abs(librosa.stft(y)) ** 2
    S = librosa.feature.melspectrogram(S=D)
    
    # Passing through arguments to the Mel filters
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                       fmax=8000)
    import matplotlib.pyplot as plt
    #print(int(len(y)/(sr)))
    plt.figure(figsize=(int(len(y)/(sr)),30))
    librosa.display.specshow(librosa.power_to_db(S,ref=np.max), fmax=8000)
    plt.tight_layout()
    plt.savefig((document[index])[: -4]+'.png', bbox_inches='tight', pad_inches = 0)

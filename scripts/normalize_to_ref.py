from os.path import join

import numpy as np
import scipy.io.wavfile
from scipy.io import wavfile
from scipy.signal import fftconvolve

from utils.utils import load_wav_files_from_directory

input_dir = r"E:\SOFA\ARI_HORIZONTAL_SYMMETRIC_AVG"
output_dir = r"E:\SOFA\ARI_HORIZONTAL_SYMMETRIC_NORMALIZED_AVG"
filename_mask = 'hrtf'

if __name__ == '__main__':
    earphones_target_wav = wavfile.read(filename=join(input_dir, 'earphones-target-48khz.wav'))
    earphones_target = earphones_target_wav[1][:, 0]
    N = len(earphones_target)
    ref_wav = wavfile.read(filename=join(input_dir, 'AVG_REF_COMP.wav'))
    # ref = np.pad(ref_wav[1], pad_width=(0,N-len(ref_wav[1])), mode='constant')
    l_fname, l_wav = load_wav_files_from_directory(input_dir=input_dir, filename_mask='AVG_A')

    # dict_hrir = {}
    u = ref_wav[1]
    for fname, wav_object in zip(l_fname, l_wav):
        azimut = int(fname.split('_A')[1].split('.wav')[0])
        v = wav_object[1]

        assert np.shape(v) == (128, 2)
        # left_ir = np.pad(wav_object[1][:,0], pad_width=(0,N-len(wav_object[1][:,0])), mode='constant')
        # right_ir = np.pad(wav_object[1][:,1], pad_width=(0,N-len(wav_object[1][:,1])), mode='constant')
        comp_hrir = fftconvolve(wav_object[1], ref_wav[1], mode='full', axes=0)
        # comp_left_fft = (fft(earphones_target) * fft(ref)) / fft(left_ir)
        # comp_right_fft = (fft(earphones_target) * fft(ref)) / fft(right_ir)
        # comp_hrir = np.transpose(np.array([ifft(comp_left_fft), ifft(comp_right_fft)]))
        scipy.io.wavfile.write(filename=join(output_dir, 'AVG_COMP_A{}.wav'.format(azimut)), rate=48000, data=comp_hrir)

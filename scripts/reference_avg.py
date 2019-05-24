from os.path import join

import numpy as np
import scipy.io.wavfile

from utils.utils import load_wav_files_from_directory

input_dir = r"E:\SOFA\ARI_HORIZONTAL_SYMMETRIC_AVG"
output_dir = r"E:\SOFA\ARI_HORIZONTAL_SYMMETRIC_AVG"
filename_mask = 'hrtf'
azimut = 5;

if __name__ == '__main__':
    _, l_wav = load_wav_files_from_directory(input_dir=input_dir)

    l_hrir = [wav_object[1] for wav_object in l_wav]
    hrir_avg = sum(l_hrir) / len(l_hrir)
    hrir_avg = np.sum(hrir_avg, axis=1)

    scipy.io.wavfile.write(join(output_dir, 'AVG_REF.wav'.format(azimut)), 48000, hrir_avg)

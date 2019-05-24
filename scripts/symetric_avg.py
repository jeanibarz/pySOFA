from os.path import join

import numpy as np
import scipy.io.wavfile

from utils.utils import load_wav_files_from_directory

input_dir = r"E:\SOFA\ARI_HORIZONTAL_AVG"
output_dir = r"E:\SOFA\ARI_HORIZONTAL_SYMMETRIC_AVG"
filename_mask = 'hrtf'

if __name__ == '__main__':
    l_fname, l_wav = load_wav_files_from_directory(input_dir=input_dir)

    dict_hrir = {}
    for fname, wav_object in zip(l_fname, l_wav):
        azimut = int(fname.split('_A')[1].split('_E')[0])
        if azimut in [0, 180]:
            dict_hrir[str(azimut)] = 0.5 * wav_object[1] + 0.5 * np.flip(wav_object[1], axis=1)
            continue
        elif azimut < 180:
            hrir = wav_object[1]
        elif azimut > 180:
            azimut = 360 - azimut
            hrir = np.flip(wav_object[1], axis=1)

        if not str(azimut) in dict_hrir.keys():
            dict_hrir[str(azimut)] = 0.5 * hrir
        else:
            dict_hrir[str(azimut)] += 0.5 * hrir

    for azimut, hrir_avg in dict_hrir.items():
        scipy.io.wavfile.write(join(output_dir, 'AVG_A{}.wav'.format(azimut)), 48000, hrir_avg)

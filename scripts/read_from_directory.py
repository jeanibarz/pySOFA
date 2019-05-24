import numpy as np
import scipy.io.wavfile

from utils.utils import get_minimum_phase, load_sofa_files_from_directory

input_dir = r"E:\SOFA\ARI"
filename_mask = 'hrtf'
azimut = 5;
elevation = 0;
radius = 1.2;

if __name__ == '__main__':
    l_sofa = load_sofa_files_from_directory(input_dir=input_dir, filename_mask=filename_mask)

    for azimut in range(180, 360, 5):
        print('Azimut {}'.format(azimut))
        l_mp_ir = []
        for sofa_object in l_sofa:
            pos_idx = sofa_object.get_source(azimut=azimut, elevation=elevation, radius=radius)
            if pos_idx:
                # print('sofa file: ' + f)
                mp_ir_left = get_minimum_phase(sofa_object.FIR.IR[pos_idx][0])
                mp_ir_right = get_minimum_phase(sofa_object.FIR.IR[pos_idx][1])

                mp_ir_left = np.reshape(mp_ir_left, (128, 1))
                mp_ir_right = np.reshape(mp_ir_right, (128, 1))

                mp_ir_stereo = np.concatenate((mp_ir_left, mp_ir_right), 1)
                l_mp_ir.append(mp_ir_stereo)
        mp_ir_avg = np.zeros_like(l_mp_ir[0])
        for mp_ir in l_mp_ir:
            mp_ir_avg += mp_ir
        mp_ir_avg = mp_ir_avg / len(l_mp_ir)
        scipy.io.wavfile.write('AVG_A{}_E{}.wav'.format(azimut, elevation), 48000, mp_ir_avg)

from os import listdir
from os.path import isfile, join

from scipy.io import wavfile
from scipy.signal import minimum_phase

import pysofa.sofa as pysofa


def load_sofa_files_from_directory(input_dir, filename_mask=''):
    """
    Read all files in the specified input_dir that contains the string filename_mask
    Return a list of SOFA objects
    :param input_dir:
    :param filename_mask:
    :return:
    """
    l_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and filename_mask in f]
    return [pysofa.SOFA(sofa_file=join(input_dir, f)) for f in l_files]


def load_wav_files_from_directory(input_dir, filename_mask=''):
    """
    Read all files in the specified input_dir that contains the string filename_mask
    Return a list of filenames and a list of wav objects
    """
    l_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and filename_mask in f]
    return [f for f in l_files], [wavfile.read(filename=join(input_dir, f)) for f in l_files]


def get_minimum_phase(ir):
    return minimum_phase(h=ir, method='homomorphic', n_fft=1024)

import numpy as np
import scipy.io
import scipy.io.wavfile
import scipy.signal
import os
import sys

sys.path.append('/om2/user/amagaro/spatial_audio_pipeline/utils')
import util_audio


def make_filtered_speech(cutoff, in_path, out_path, batch_num):
    batch_size = 250

    files = os.listdir(in_path)
    print(len(files))

    for clip_ii in range(batch_num*batch_size, min(batch_num*batch_size + batch_size, len(files))):
        input_file = in_path + files[clip_ii]
        fname = files[clip_ii].split('.wav')[0]
        sr, loud_audio = scipy.io.wavfile.read(input_file)
        audio = util_audio.set_dBSPL(loud_audio, 60.0)
        new_audio_lowpass = filter_cutoff(cutoff, audio, sr, 'lowpass')
        new_audio_highpass = filter_cutoff(cutoff, audio, sr, 'highpass')
        scipy.io.wavfile.write(out_path + 'lowpass/' + fname + '_' + str(cutoff) + '_Hz_' + 'lowpass.wav', sr, np.array(new_audio_lowpass, dtype=np.float32))
        scipy.io.wavfile.write(out_path + 'highpass/' + fname + '_' + str(cutoff) + '_Hz_' + 'highpass.wav', sr, np.array(new_audio_highpass, dtype=np.float32))


def filter_cutoff(cutoff, signal, sr, filt_type='lowpass'):
    filt = scipy.signal.firwin(numtaps=2001, cutoff=cutoff, pass_zero=filt_type, fs=sr)
    result = scipy.signal.lfilter(filt, 1.0, signal)
    return result


def main():
    cutoffs = [200, 400, 800, 1600, 3200, 6400]
    batch_num = int(sys.argv[1])
    input_dir = '/om/user/alexkell/psychophysics_stim_2016X/2017W-word-forNetwork/selected-stim-with-NO-bg/'
    output_dir = '/om/scratch/Wed/amagaro/'
    for cutoff in cutoffs:
        make_filtered_speech(cutoff, input_dir, output_dir, batch_num)


if __name__ == '__main__':
    main()
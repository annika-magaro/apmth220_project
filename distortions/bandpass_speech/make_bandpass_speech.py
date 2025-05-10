import numpy as np
import scipy.io
import scipy.io.wavfile
import scipy.signal
import os
import sys

sys.path.append('/om2/user/amagaro/spatial_audio_pipeline/utils')
import util_audio


def make_bandpass_speech(num_semitones, in_path, out_path, batch_num):
    batch_size = 250
    center = 1500

    files = os.listdir(in_path)
    print(len(files))
    low, high = get_bounds(center, num_semitones)

    for clip_ii in range(batch_num*batch_size, min(batch_num*batch_size + batch_size, len(files))):
        input_file = in_path + files[clip_ii]
        fname = files[clip_ii].split('.wav')[0]
        sr, loud_audio = scipy.io.wavfile.read(input_file)
        audio = util_audio.set_dBSPL(loud_audio, 60.0)
        new_audio = filter_bandpass(low, high, audio, sr)
        scipy.io.wavfile.write(out_path + fname + '_' + str(num_semitones) + '_' + 'bandpass.wav', sr, np.array(new_audio, dtype=np.float32))


def filter_bandpass(low, high, signal, sr):
    filt = scipy.signal.firwin(numtaps=2001, cutoff=(low, high), pass_zero='bandpass', fs=sr)
    result = scipy.signal.lfilter(filt, 1.0, signal)
    return result


def get_bounds(center, num_semitones):
    high = center * 2**(num_semitones/24)
    low = center / 2**(num_semitones/24)
    return low, high


def main():
    widths = np.arange(3, 60)
    batch_num = int(sys.argv[1])
    input_dir = '/om/user/alexkell/psychophysics_stim_2016X/2017W-word-forNetwork/selected-stim-with-NO-bg/'
    output_dir = '/om/scratch/Wed/amagaro/bandpass/'
    for k in widths:
        make_bandpass_speech(k, input_dir, output_dir, batch_num)


if __name__ == '__main__':
    main()
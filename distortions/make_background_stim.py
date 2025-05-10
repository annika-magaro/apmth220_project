import os
import numpy as np
import scipy
import soundfile as sf
import sys
import soxr
import argparse
import glob

sys.path.append('/om2/user/msaddler/python-packages/msutil')
import util_stimuli


def make_background_stim(bg_src_dir, fg_src_dir, dst_dir, snrs):
    bg_files = os.listdir(bg_src_dir)
    bg_wavs = [i for i in bg_files if '.wav' in i]
    fg_files = os.listdir(fg_src_dir)
    bg_dict = {}
    for i, fg in enumerate(fg_files):
        bg_index = i%len(bg_wavs)
        bg = bg_wavs[bg_index]
        fg_sr, fg_wav = scipy.io.wavfile.read(fg_src_dir + fg)
        bg_sr, bg_wav = scipy.io.wavfile.read(bg_src_dir + bg)
        bg_wav_rs = soxr.resample(bg_wav, bg_sr, fg_sr) 
        bg_wav_trimmed = bg_wav_rs[len(bg_wav_rs)//2-len(fg_wav)//2:len(bg_wav_rs)//2+len(fg_wav)//2]
        fg_wav_normalized = util_stimuli.set_dBSPL(fg_wav, 60.0)
        bg_name = bg[:-4]
        fg_name = fg[:-4]
        bg_dict[fg_name] = bg_name
        for snr in snrs:
            if snr == 'inf':
                wav_normalized = fg_wav_normalized
            else:
                bg_wav_normalized = util_stimuli.set_dBSPL(bg_wav_trimmed, 60.0 - snr)
                wav = fg_wav_normalized + bg_wav_normalized
                wav_normalized = util_stimuli.set_dBSPL(wav, 60.0)
            sf.write(f'{dst_dir}{fg_name}_{snr}dB.wav', wav_normalized, fg_sr, subtype='FLOAT')
    return bg_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generate modulated bg tfrecords')
    parser.add_argument('-j', '--job_idx', type=int, default=0)
    args = vars(parser.parse_args())
    filenum = int(args['job_idx'])

    bg_dir = '/om2/user/msaddler/spatial_audio_pipeline/assets/human_experiment_v00/synthetic_textures/'
    subdirs = [f"{i:03}" for i in range(43)]#['ieeeaaspcasa', 'cv08talkerbabble', 'musdb18hq', 'issnstationary', 'issnfestenplomp']
    fg_src_dir = '/om2/user/amagaro/spatial_audio_pipeline/wavs/230_words/'
    dst_superdir = '/om/scratch/Wed/amagaro/wavs/43_textures_new/'
    dst_subdirs = ['neg3'] #[f"{i:02}" for i in range(43)] #['audscene', 'babble', 'music', 'stat_noise', 'mod_noise']
    snrs = [-3] #[-9, -6, -3, 0, 3, 'inf']
    bg_src_dir = glob.glob(f'{bg_dir}{subdirs[filenum]}_*')[0] + '/'
    #bg_src_dir = f'{bg_dir}background_{subdirs[filenum]}/'
    dst_dir = f'{dst_superdir}{dst_subdirs}/'
    bg_dict = make_background_stim(bg_src_dir, fg_src_dir, dst_dir, snrs)
    json.dump(bg_dict, open(f'{filenum:02}_fname_to_bg_2.json', 'w'))



import json
import numpy as np
import os
from scipy.io import wavfile
import shutil
from config import *

conditions = ['lowpass', 'highpass', 'bandpass', 'audscene', 'babble', 'music', 'stat-noise', 'mod-noise', 'specmod', 'tempmod', 'shuffled',
              'compressed-dilated', 'cognitive-restoration', 'sine-wave-speech', 'whispered', 'inharmonic', 'noise-vocoded', 
              'synth-reverb-drr-20', 'synth-reverb-drr-50', 'unfiltered']

superdirs = ['audio_filtering'] * 3 + ['backgrounds'] * 5 + ['spectemp_mod'] * 2 + ['shuffled_clipped', 'compressed_dilated', 'local_time_reversal'] + ['swin'] * 4 + ['reverb'] * 2 + [None]
num_conditions = 3
chosen_fnames = {}
for i in range(num_conditions):
    with open(f'chosen_filenames_compressed_dilated/{i:02d}.json') as f:
        chosen_fnames[i] = json.load(f) 

for superdir, condition in zip(superdirs[-1:], conditions[-1:]):
    print("starting " + condition)
    src_dir = directories[condition]
    if condition == 'unfiltered':
        dir_dst = f'/om/scratch/Wed/amagaro/apmth220_project/wavs/clean/'
    else:
        dir_dst = f'/om/scratch/Wed/amagaro/apmth220_project/wavs/{directories[condition].split("wavs")[-1]}/'
    condition_names = []
    if condition == 'unfiltered':
        condition_names.append(None)
    else:
        for param in experimental_conditions[superdir][condition]:
            condition_names.append(f'{condition}_{param}')

    for i in range(num_conditions):
        for fname in chosen_fnames[i]:
            if condition == 'unfiltered':
                src_fn = chosen_fnames[i][fname] + '.wav'
                shutil.copy2(src_dir + src_fn, dir_dst + src_fn)
            else:
                for cond in condition_names:
                    cond_type, setting = cond.split('_')
                    src_fn = chosen_fnames[i][fname] + '_' + tag_fn[cond_type](setting) + '.wav'
                    shutil.copy2(src_dir + src_fn, dir_dst + src_fn)


day = "Wed"
file_dir = f"/om/scratch/{day}/amagaro/wavs/"

experimental_conditions = {
    "audio_filtering": {
        "lowpass": [400, 800, 1600, 3200],
        "highpass": [400, 800, 1600, 3200, 6400],
        "bandpass": [5, 10, 20, 30, 40],
        "unfiltered": True
    }, 
    "spectemp_mod": {
        "specmod": [0.5, 1, 2, 4, 8],
        "tempmod": [3, 6, 12, 24],
        "unfiltered": True
    },
    "repackaged_silenced": {
        "repackaged": [0.25, 0.5, 1, 2, 4],
        **{f"silenced-{x}": [1, 3, 10, 30, 100] for x in [0.25, 0.5, 0.75]}, 
        "compressed-dilated": [0.5],
        "unfiltered": False
    },
    "masked": {
        **{f"masked-{x}": [-18, -9, 0, 9] for x in [1, 3, 10, 30, 100]},
        "unfiltered": False
    },
    "chimera": {
        "speech": [1, 2, 4, 8, 16],
        "noise": [1, 2, 4, 8, 16],
        "unfiltered": False
    },
    "shuffled_clipped": {
        "shuffled": [0.125, 0.25, 0.5, 1, 2, 4],
        "peak-clipped": [0, 0.25, 0.5, 0.75, 0.9, 0.98],
        "center-clipped": [0, 0.25, 0.5, 0.75, 0.9, 0.98],
        "unfiltered": False
    },
    "swin": {
        "sine-wave-speech": [4],
        "whispered": [1],
        "inharmonic": [10, 30, 50],
        "noise-vocoded": [1, 2, 4, 8, 16, 32],
        "unfiltered": True
    },
    "reverb": {
        "synth-reverb-drr-20": [200, 400, 800, 1600], ## FILL OUT ##
        "synth-reverb-drr-50": [200, 400, 800, 1600],
        "synth-reverb-babble-drr-20": [200, 400, 800, 1600],
        "synth-reverb-babble-drr-50": [200, 400, 800, 1600],
        "unfiltered": False
    },
    "compressed_dilated": {
        "compressed-dilated": [0.5, 0.75, 0.875, 1.25, 1.5, 2],
        "unfiltered": True
    },
    "local_time_reversal": {
        "cognitive-restoration": [10, 20, 30, 40, 50, 100, 150, 200],
        "unfiltered": False
    },
    "backgrounds": {
        "audscene": [-9, -6, -3, 0, 3],
        "babble": [-9, -6, -3, 0, 3],
        "music": [-9, -6, -3, 0, 3],
        "stat-noise": [-9, -6, -3, 0, 3],
        "mod-noise": [-9, -6, -3, 0, 3],
        "unfiltered": True
    },
    "43_textures": {
        "43-textures": [x for x in range(43)],
        "unfiltered": False
    }
}

directories = {
    "lowpass": f"{file_dir}/lowpass/",
    "highpass": f"{file_dir}/highpass/",
    "bandpass": f"{file_dir}/bandpass/",
    "specmod": f"{file_dir}/mod_lowpass/specmod/",
    "tempmod": f"{file_dir}/mod_lowpass/tempmod/",
    "repackaged": f"{file_dir}/repackaged/",
    **{f"silenced-{x}": f"{file_dir}/silenced/{x}/" for x in [0.25, 0.5, 0.75]},
    "compressed-dilated": f"{file_dir}/compressed_dilated/",
    **{f"masked-{x}": f"{file_dir}/masked/{x}/" for x in [1, 3, 10, 30, 100]},
    "speech": f"{file_dir}/chimera/",
    "noise": f"{file_dir}/chimera_noise/",
    "shuffled": f"{file_dir}/shuffled/",
    "peak-clipped": f"{file_dir}/peak_clipping/",
    "center-clipped": f"{file_dir}/center_clipping/",
    "sine-wave-speech": f"{file_dir}/sine_wave_speech/",
    "whispered": f"{file_dir}/whispered/",
    "inharmonic": f"{file_dir}/inharmonic/",
    "noise-vocoded": f"{file_dir}/noise_vocoded/",
    "synth-reverb-drr-20": f"{file_dir}/synth_reverb/20/",
    "synth-reverb-drr-50": f"{file_dir}/synth_reverb/50/",
    "synth-reverb-babble-drr-20": f"{file_dir}/synth_reverb_babble_0dB/20/",
    "synth-reverb-babble-drr-50": f"{file_dir}/synth_reverb_babble_0dB/50/",
    "compressed-dilated": f"{file_dir}/compressed_dilated/",
    "cognitive-restoration": f"{file_dir}/cognitive_restoration/",
    "audscene": f"{file_dir}/backgrounds/audscene/",
    "babble": f"{file_dir}/backgrounds/babble/",
    "music": f"{file_dir}/backgrounds/music/",
    "stat-noise": f"{file_dir}/backgrounds/stat_noise/",
    "mod-noise": f"{file_dir}/backgrounds/mod_noise/",
    "43-textures": f"{file_dir}/43_textures/snr_-3/",
    "unfiltered": "/om2/user/amagaro/spatial_audio_pipeline/wavs/source_files/"
}

tag_fn = {
    "lowpass": lambda x: f"{x}_Hz_lowpass",
    "highpass": lambda x: f"{x}_Hz_highpass",
    "bandpass": lambda x: f"{x}_bandpass",
    "specmod": lambda x: f"specmod_lowpass_{x}",
    "tempmod": lambda x: f"tempmod_lowpass_{x}",
    "repackaged": lambda x: f"0.5_compressed_dilated_0.5_{x}_repackaged",
    **{f"silenced-{y}": lambda x: f"{x}_rampedsilenced" for y in [0.25, 0.5, 0.75]},
    "compressed-dilated": lambda x: f"{x}_compressed_dilated_{x}",
    "speech": lambda x: f"{x}_chimera",
    "noise": lambda x: f"{x}_chimera_fs",
    "shuffled": lambda x: f"{x}_shuffled",
    "peak-clipped": lambda x: f"{x}_peakclipped",
    "center-clipped": lambda x: f"{x}_centerclipped",
    "sine-wave-speech": lambda x: f"{x}_bands",
    "whispered": lambda x: f"whisp",
    "inharmonic": lambda x: f"inharm_jitt{x}",
    "noise-vocoded": lambda x: f"{x}_numChannels",
    "synth-reverb-drr-20": lambda x: f"0.5_synth_reverb_{x}ms_20drr",
    "synth-reverb-drr-50": lambda x: f"0.5_synth_reverb_{x}ms_50drr",
    "synth-reverb-babble-drr-20": lambda x: f"8_speaker_babble_0dB_synth_reverb_{x}ms_20drr",
    "synth-reverb-babble-drr-50": lambda x: f"8_speaker_babble_0dB_synth_reverb_{x}ms_50drr",
    "compressed-dilated": lambda x: f"{x}_compressed_dilated_{x}",
    "cognitive-restoration": lambda x: f"{x}_segmentLength",
    "audscene": lambda x: f"{x}dB",
    "babble": lambda x: f"{x}dB",
    "music": lambda x: f"{x}dB",
    "stat-noise": lambda x: f"{x}dB",
    "mod-noise": lambda x: f"{x}dB",
    "43-textures": lambda x: f"{int(x):02}",
    **{f"masked-{y}": lambda x: f"{x}_masked" for y in [1, 3, 10, 30, 100]}
}



function make_compressed_dialated_speech_v2(batch_no, ratio, in_path, output_dir)

% Wrapper to make compressed dilated speech by making a call to Joshs praat_change_speed.praat script
% s indexes the different speed_ratios to allow for stim to be generated in parallel 
batch_size = 400
callpraat =  '/om2/user/amagaro/network_analyses_2023/scripts_to_generate_psychophysics_stim/compressed_dialated/praat_barren'

if nargin < 4
    output_dir = '/om/scratch/Wed/amagaro/compressed_dilated/';
    in_path = '/om/scratch/Wed/amagaro/wavs_for_compressed_dilated/';
end

input_dir = strcat(in_path, ratio, '/')
%input_dir = '/om/user/alexkell/psychophysics_stim_2016X/2017W-word-forNetwork/selected-stim-with-NO-bg/';
%output_dir = '/om/scratch/Wed/amagaro/compressed_dilated/';
%input_dir = '/om/scratch/Wed/amagaro/wavs_for_compressed_dilated/0.5/';
%input_dir = '/nobackup/scratch/Sun/amagaro2/amagaro/dry_wavs_for_compressed_dilated/';
%input_dir = '/om2/user/ershook/spring_18/makePsychophysicsStimuli/wavs_for_compressed_dialated_remove_apostrophe/';
%input_dir = '/om2/user/ershook/spring_18/makePsychophysicsStimuli/fixed_names/'
%output_dir = '/om2/user/ershook/spring_18/makePsychophysicsStimuli/compressed_dialated_fix_names/';
%input_dir = '/om/scratch/Tue/ershook/raw_wav_temp/'
%output_dir = '/om/scratch/Tue/ershook/compressed_dilated_temp/'
%input_dir = '/om/scratch/Tue/ershook/compressed_dilated_fixed_names/'
%input_dir = '/om/scratch/Tue/ershook/compressed_dilated_twice_rename/'
%output_dir = '/om/scratch/Tue/ershook/compressed_dilated_fixed_names_output/'
%output_dir = '/om/scratch/Tue/ershook/compressed_dilated_twice_rename_output/'
%speed_ratios = {'0.5', '0.75', '0.875', '1.25', '1.5', '2'} %{'0.5'} %{'0.3', '0.4', '0.5', '0.6', '0.7'} %  %'0.75', '0.825', '1.25', '1.5', '2'};

files = dir(input_dir)
len = length(files)
speed_ratio = ratio %speed_ratios{1}

for clip_ii= batch_no*batch_size+3:min(len, batch_no*batch_size+3+ batch_size-1)  %Ignore '.' and '..' so start at 3
%for clip_ii = 2+s:6:len
    input_file = strcat(input_dir, files(clip_ii).name) 
    fname = strsplit(files(clip_ii).name, '.wav')
    output_file = strcat(output_dir, fname{1}, char('_compressed_dilated_'), speed_ratio, char('.wav'))


    unix([callpraat ' /om2/user/amagaro/network_analyses_2023/scripts_to_generate_psychophysics_stim/compressed_dialated/praat_change_speed.praat ' input_file ' ' output_file ' ' speed_ratio], '-echo');

    end
end

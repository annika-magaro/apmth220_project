
function make_compressed_dialated_speech(s)

% Make compressed dialated speech using Praat by making a call to Josh's praat_change_speed.praat script
% s indexes the different speed_ratios to allow for stim to be generated in parallel 

input_dir = '/om/user/alexkell/psychophysics_stim_2016X/2017W-word-forNetwork/selected-stim-with-NO-bg/';
output_dir = '/om2/user/ershook/spring_18/makePsychophysicsStimuli/compressed_dialated/';


callpraat =  './praat_barren'

speed_ratios = ['0.5', '0.75', '0.825', '1.25', '1.5', '2'];

files = dir(input_dir);

for clip_ii= 3:length(files) %Ignore '.' and '..' so start at 3

    speed_ratio = speed_ratios(s); 
    input_file = strcat(input_dir, '/', files(clip_ii).name); 
    fname = strsplit(files(clip_ii).name, '.wav')
    output_file = strcat(output_dir, fname, '_compressed_dialated_', num2str(speed_ratio), '.wav');
    strcat(callpraat, ' praat_change_speed.praat ', input_file, ' ', output_file, ' ', speed_ratio)
    unix(strcat(callpraat, ' praat_change_speed.praat ', char(input_file), ' ', char(output_file), ' ', char(speed_ratio)) , '-echo');

    end
end

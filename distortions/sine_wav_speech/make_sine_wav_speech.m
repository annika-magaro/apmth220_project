

function make_sine_wav_speech(batch_no, num_bands, input_dir, output_dir)

    if nargin < 3
        input_dir = '/om/scratch/Wed/amagaro/saganet_testing/clean2/'; %'/om/user/alexkell/psychophysics_stim_2016X/2017W-word-forNetwork/selected-stim-with-NO-bg/';
        output_dir = '/om/scratch/Wed/amagaro/saganet_testing/sine_wave_speech/';
    end
    
    batch_size = 1000;
    output_dir_wav = output_dir; %strcat(output_dir, '/wavs');
    output_dir_plot = strcat(output_dir, '/plots/');
    
    files = dir(input_dir);

    for clip_ii= batch_no*batch_size+3:batch_no*batch_size+3+batch_size-1 

        input_file = strcat(input_dir, files(clip_ii).name) 
        fname = strsplit(files(clip_ii).name, '.wav')

        [d,r] = audioread(input_file);
        d = (d/rms(d)) *.1;
        try
        d = d(:,1);
        [F,M] = swsmodel(d,r);

        dr = synthtrax(F(1:num_bands,:),M,r);
        %figure1 = figure()
        %subplot(211)
        %specgram(d,256,r);
        %title('Original')
        %subplot(212)
        %specgram(dr,256,r);
        %title('Sine wave replica');
        [output_dir_wav  '/', fname{1}, '_', num2str(num_bands), '_bands.wav']
        dr = (dr/rms(dr))*.05; 
        wavwrite(dr,r,[output_dir_wav  '/', fname{1}, '_', num2str(num_bands), '_bands.wav']);
       % saveas(figure1,[output_dir_plot  '/', fname{1},'_', num2str(num_bands), '_bands.png']);
        except
            'problem'
        end
    end
end


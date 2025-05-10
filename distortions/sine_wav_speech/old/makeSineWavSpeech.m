

function makeSineWavSpeech(batch_no)
    load('wav_paths.mat');
    load('output_names.mat');
    utterances = string(wavs);
    output_dir_wav = '/om/user/ershook/spring_18/NetworkAnalyses/sine_wave_speech/synth_speech';
    output_dir_plot = '/om/user/ershook/spring_18/NetworkAnalyses/sine_wave_speech/plots';

    for i=  1:length(utterances)%batch_no*batch_size+1:batch_no*batch_size+1+batch_size %length(utterances) %loop through your speech clips

        filename = strcat(utterances(i,:))
        [d,r] = audioread(filename);

        [F,M] = swsmodel(d,r);
        'length'
        size(F)
        dr = synthtrax(F(1:1,:),M,r);
        figure1 = figure()
        subplot(211)
        specgram(d,256,r);
        title('Original')
        subplot(212)
        specgram(dr,256,r);
        title('Sine wave replica');
        
        word = strcat(output_names(i,:));
        wavwrite(dr,r,[output_dir_wav  '/' word '_sine_wav_speech_3Bands.wav']);
        saveas(figure1,[output_dir_plot  '/' word '_sine_wav_speech_spectrogram_3Bands.png']);
    end
end

form 
    text inputfile
    text outputfile
    real speed_ratio
endform

#echo 'inputfile$'
wav = Read from file... 'inputfile$'

select wav
new_wav = Lengthen (overlap-add)... 75 600 'speed_ratio'

select new_wav
Save as WAV file... 'outputfile$'


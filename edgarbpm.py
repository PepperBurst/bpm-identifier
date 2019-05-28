import librosa

def getBPM(filename):
    # filename = "songs/80 BPM.mp3" #used for importing song. File should be in the same folder of this script.
    y, sr = librosa.load(filename) #loading to library
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr) #for gathering tempo marking data
    # print('Tempo: {:.2f}' .format(tempo)) #print of tempo markings
    tempoMarking = ''
    terms = ''
    if tempo >= 168 and tempo <= 208:
        tempoMarking = 'Presto'
        terms = 'Very fast'
        # print("The genre of this song can be Presto, which means very fast in English")
    elif tempo >= 120 and tempo <= 168:
        tempoMarking = 'Allegro'
        terms = 'Fast'
            # print("The genre of this can be Allegro, which means fast in English")
    elif tempo >= 108 and tempo <= 120:
        tempoMarking = 'Moderato'
        terms = 'Moderate speed'
            # print("The genre of this can be Moderato, which means moderate speed in English")        
    elif tempo >= 76 and tempo <= 108:
        tempoMarking = 'Andante'
        terms = 'Moderate walking speed'
            # print("The genre of this can be Andante, which means moderate walking speed in English")        
    elif tempo >= 66 and tempo <= 76:
        tempoMarking = 'Adagio'
        terms = 'Slow'
            # print("The genre of this can be Adagio, which means slow in English")        
    elif tempo >= 40 and tempo <= 66:
        tempoMarking = 'Lagro'
        terms = 'Slow and solemn'
            # print("The genre of this can be Lagro, which means slow and solemn in English")
    return tempo, tempoMarking, terms
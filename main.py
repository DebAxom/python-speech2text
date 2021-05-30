import sys
import speech_recognition as sr
filename = sys.argv[1]
textfilename = filename.split('.')[0]+'.txt'
r = sr.Recognizer()
try:
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        f = open(textfilename, "w")
        f.write(text)
        print("Converted Speech to Text successfully!")
except:
    print('An error occured. Please check if the audio file exists or not!')        
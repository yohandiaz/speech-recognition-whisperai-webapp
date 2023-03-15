import fileLoader as fl
import pathlib

import whisper

model = whisper.load_model("small")

def audioToText(file_path):
    
    convertedFileName = fl.load_audio_file(file_path)
    
    return model.transcribe(convertedFileName)["text"]

    """import speech_recognition as sr


    engine = sr.Recognizer()

    # read mp3 file
    def audioToText(file_path):
        
        # Converts the audio file to wav format if it is not
        convertedFileName = fl.load_audio_file(file_path)

        with sr.AudioFile(convertedFileName) as source:
            print('Analyzing file...')
            audio = engine.record(source)

        # extract and print text

        text = engine.recognize_google(audio, language="fr-FR")
        print(f'Text: {text}')
        txtFile = open('textRecognized.txt', 'w')
        txtFile.writelines(text)
        with open('textRecognized.txt', 'r') as txtFile:
            return txtFile.read()"""
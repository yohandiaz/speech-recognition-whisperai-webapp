import fileLoader as fl
import pathlib

import whisper

model = whisper.load_model("base")

def addBreaklines(text):
    chars = list(text)

    # Loop through each index in the character list
    for i in range(len(chars)):
        # If the current character is a '?' character, insert a line break after it
        if chars[i] == '?':
            chars[i] = '?\n\n'

    # Convert the list of characters back into a string and return it
    return ''.join(chars)

def audioToText(file_path):
    
    convertedFileName = fl.load_audio_file(file_path)
    
    return model.transcribe(convertedFileName)["text"]
#    result = model.transcribe(convertedFileName)["text"]

#    return addBreakLines(result)

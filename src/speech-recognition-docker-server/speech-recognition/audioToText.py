import fileLoader as fl
import pathlib

from speechToText import audioToText


audio_file_path = str(pathlib.Path(__file__).parent.parent.resolve()) + "/flask/"
audio_file_path += input("Insert the name of the file: ")

audioToText(audio_file_path)
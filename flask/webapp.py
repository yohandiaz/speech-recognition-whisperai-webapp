from flask import Flask, request, render_template
import sys

sys.path.append('../speech-recognition')
from speechToText import audioToText
sys.path.pop(sys.path.index('../speech-recognition'))

# Manage user session
userId = 0

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/audio_to_text', methods=['POST'])
def audio_to_text():
    # Get the uploaded file from the HTML form
    audio_file = request.files['audio_file']

    # Save the uploaded file to the server
    audio_file_path = audio_file.filename
    audio_file.save(audio_file_path)

    # Transcribe the audio to text
    return audioToText(audio_file_path)

    return render_template('result.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="18500")

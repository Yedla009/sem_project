from flask import Flask, request, send_file
import speech_recognition as sr
import pyttsx3
# from pydub import AudioSegment
import os

app = Flask(__name__)

# Initialize the recognizer
r = sr.Recognizer()

def synthesize_text_to_speech(text, output_filename):
    """Synthesizes speech from text and saves to a file."""
    engine = pyttsx3.init()
    engine.save_to_file(text, output_filename)
    engine.runAndWait()

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return "Audio file is required.", 400

    audio_file = request.files['audio']
    print("n audiofile received")
    audio_filename = audio_file.filename

    # Save the audio file temporarily
    audio_path = os.path.join('uploads', audio_filename)
    audio_file.save(audio_path)

    # format = audio_file.filename.split('.')[-1]
    # audio = AudioSegment.from_file(audio_path, format="3gp")
    # # wavPath = audio_path.rsplit('.', 1)[0] + '.wav'
    # audio.export("output.wav", format="wav")

    try:
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)  # Read the entire audio file
            command = r.recognize_google(audio)  # Recognize speech
            print(f"Recognized command: {command}")

            # Process the command to generate response text
            if "hello" in command.lower():
                response_text = "Hello! How can I help you?"
            elif "what is your name" in command.lower():
                response_text = "I am your Python assistant."
            else:
                response_text = "Sorry, I didn't catch that."

            # Synthesize response to audio
            response_audio_filename = "response.mp3"
            response_audio_path = os.path.join('responses', response_audio_filename)
            synthesize_text_to_speech(response_text, response_audio_path)

            # Clean up the original audio file
            os.remove(audio_path)

            return send_file(response_audio_path, as_attachment=True)

    except Exception as e:
        print("fuckup")
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

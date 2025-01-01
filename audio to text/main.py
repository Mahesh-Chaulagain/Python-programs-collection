# pip install SpeechRecognition pydub

import speech_recognition as sr

recognizer = sr.Recognizer()

audio_file = "audiobook.wav"

from pydub import AudioSegment
AudioSegment.from_mp3(audio_file).export(audio_file, format='wav')

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("Extracted Text: ", text)

except sr.UnknownValueError:
    print("Could not understand the audio")

except sr.RequestError as e:
    print("API Error: ", e)
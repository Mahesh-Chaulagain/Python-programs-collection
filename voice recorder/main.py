import sounddevice

from scipy.io.wavfile import write

# sample rate
fs = 44100

second = int(input('Enter the recording time in seconds:'))
print('Recording...\n')
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write('MyRecording.wav', fs, record_voice)
print('Recording is done. Please check your folder to listen recording')
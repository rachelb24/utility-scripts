import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio_path = "your_audio_file.wav"
y, sr = librosa.load(audio_path)

D = librosa.stft(y)

plt.figure(figsize=(10, 6))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                        sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()

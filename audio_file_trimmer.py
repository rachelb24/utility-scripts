import soundfile as sf
import librosa

def trim_audio(input_path, output_path, start_time, end_time):

   y, sr = sf.read(input_path)

   start_sample = int(start_time * sr)
   end_sample = int(end_time * sr)

   trimmed_audio = y[start_sample:end_sample]

   sf.write(output_path, trimmed_audio, sr)

input_file = "your_audio_file.wav"
output_file = "trimmed_audio_file.wav"
start_time = 13  # Enter your start time in seconds
end_time = 59    # Enter your end time in seconds

trim_audio(input_file, output_file, start_time, end_time)

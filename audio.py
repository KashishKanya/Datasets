# audio_quick_inspect.py
import pandas as pd
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

AUDIO_PATH = "audio.mp3"

# Load (mono) - sr=None preserves original sample rate
y, sr = librosa.load(AUDIO_PATH, sr=None, mono=True)

# "First 5 rows" (first 5 samples)
print("First 5 samples:")
print(y[:5])

# File / dataset info
info = sf.info(AUDIO_PATH)
print("\nFile info:")
print(f"Path: {AUDIO_PATH}")
print(f"Sample rate: {sr} Hz, Frames: {info.frames}, Duration: {info.frames/sr:.2f} s")

# Convert to pandas Series to use .info()/.describe()-like methods
s = pd.Series(y)
print("\nSeries info:")
print(s.info())         # similar to df.info()
print("\nStatistics (describe):")
print(s.describe())     # similar to df.describe()

# Simple scatter plot: time vs amplitude (like your iris scatter)
times = (s.index / sr)
plt.scatter(times, s, s=1)   # s=1 makes points small
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio: Time vs Amplitude (scatter)")
plt.xlim(0, min(5, times.max()))  # show only first 5 seconds for clarity (optional)
plt.show()

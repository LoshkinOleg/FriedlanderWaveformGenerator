import math
import numpy as np
from scipy.io.wavfile import write
import argparse

parser = argparse.ArgumentParser(description="Python script for generating the Friedlander waveform in .wav format. Maximal pressure is assumed to be 1 . Output wav file format is at whatever samplerate you specify with 32-bit float quantization.")
parser.add_argument("time_at_neg_phase", metavar="time_at_neg_phase", type=float, nargs="+", help="Time at which the pressure goes into the negative. Float.")
parser.add_argument("duration", metavar="duration", type=float, nargs="+", help="Time in seconds between the shockwave onset and the end of the audio data. Float.")
parser.add_argument("samplerate", metavar="samplerate", type=int, nargs="+", help="Samplerate of the output wav file. Integer.")
parser.add_argument("prepend_padding", metavar="prepend_padding", type=float, nargs="+", help="Time in seconds leading to the shockwave. Does not contribute to duration. Float.")
parser.add_argument("fade_out", metavar="fade_out", type=bool, nargs="+", help="Whether or not to fade the tail of the waveform out to zero. Fades out linearly from time_at_neg_phase to end of waveform. Boolean.")
parser.add_argument("filename", metavar="filename", type=str, nargs="+", help="Name of the output file with extension. String.")
args = parser.parse_args()

max_pressure = 1.0
time_at_neg_phase = args.time_at_neg_phase
duration = args.duration
samplerate = args.samplerate
prepend_padding = samplerate * args.prepend_padding
fade_out = args.fade_out
filename = args.filename

nr_of_samples = samplerate * duration
step = 1.0 / samplerate
waveform = []

# Pad the beginning.
for i in range(prepend_padding):
    waveform.append(0.0)

# Generate the Friedlander data.
for i in range(nr_of_samples):
    waveform.append(max_pressure * math.exp(-(i * step) / time_at_neg_phase) * (1.0 - ((i * step) / time_at_neg_phase)))

# Fade out.
if fade_out:
    pass

# Write to file.
write(filename, samplerate, np.asarray(waveform).astype(np.float32))
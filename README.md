# Friedlander Waveform Generator
A python script for generating a [Friedlander Waveform](https://en.wikipedia.org/wiki/Blast_wave). Generates a 32-bit wav file at the specified samplerate containing a generated Friedlander graph.

# Usage
"python friedlander.py <time_at_neg_phase> <duration> <samplerate> <prepend_padding> <fade_out> <filename>" <br>
See "python friedlander.py -h" for more details.

# Dependancies
Python modules dependancies:
- numpy
- scipy
- argparse
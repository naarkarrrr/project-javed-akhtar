import torch
from torch.serialization import add_safe_globals
import numpy as np

add_safe_globals([np.core.multiarray.scalar])

from bark import SAMPLE_RATE, generate_audio, preload_models
import soundfile as sf

preload_models()

text = "Aaj phir dil ne ek nayi dastaan likhi hai..."
audio_array = generate_audio(text)
sf.write("bark_output.wav", audio_array, SAMPLE_RATE)

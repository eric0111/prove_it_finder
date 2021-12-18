import torch
import librosa
import numpy as np
from scipy.io import wavfile
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


def generate_transcription(output_audio_f):
    fun_name = 'generate_transcription'
    print(fun_name + ' started')

    # data = wavfile.read(output_audio_f)
    # framerate = data[0]
    # sounddata = data[1]
    # time = np.arange(0, len(sounddata)) / framerate
    input_audio, _ = librosa.load(output_audio_f, sr=16000)
    input_values = tokenizer(input_audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]

    print(fun_name + ' finished')
    return transcription


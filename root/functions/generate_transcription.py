import torch
import librosa


def generate_transcription(output_audio_f, tokenizer, model):
    fun_name = 'generate_transcription'
    print(fun_name + ' started')

    input_audio, _ = librosa.load(output_audio_f, sr=16000)
    input_values = tokenizer(input_audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    #print(transcription)

    print(fun_name + ' finished')
    return transcription


import librosa


def generate_letters_at_sec(file_name, transcription):
    duration = librosa.get_duration(filename=file_name)
    letters = len(transcription)

    let_at_sec = int(letters / duration)
    return let_at_sec

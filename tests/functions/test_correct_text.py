from unittest import TestCase

from functions.correct_text import correct_text
from functions.generate_transcription import generate_transcription
from functions.select_and_generate_audio import select_and_generate_audio


class Test(TestCase):
    def test_correct_text(self):
        folder = '/home/eb/Videos/arf/'
        file_input = 'test_input.mp4'
        file_output = 'test_output.mp4'

        output_audio_f = select_and_generate_audio(folder, file_input, file_output)
        transcription = generate_transcription(output_audio_f)
        transcription_updated = correct_text(transcription)

        print(transcription, transcription_updated)

from unittest import TestCase

from functions.generate_transcription import generate_transcription
from functions.select_and_generate_audio import select_and_generate_audio


class Test(TestCase):
    def test_generate_transcription(self):
        folder = '/home/eb/Videos/arf/'
        file_input = 'test_input.mp4'
        file_output = 'test_output.mp4'

        output_audio_f = select_and_generate_audio(folder, file_input, file_output)
        out = generate_transcription(output_audio_f)
        print(out)



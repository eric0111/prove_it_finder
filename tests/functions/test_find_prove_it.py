from unittest import TestCase

from functions.correct_text import correct_text
from functions.find_in_text import find_in_text
from functions.generate_transcription import generate_transcription
from functions.select_and_generate_audio import select_and_generate_audio


class Test(TestCase):
    def test_find_prove_it(self):
        folder = '/home/eb/Videos/arf/'
        file_input = 'test_input.mp4'
        file_output = 'test_output.mp4'
        to_find = 'prove'

        output_audio_f = select_and_generate_audio(folder, file_input, file_output)
        transcription = generate_transcription(output_audio_f)
        transcription_updated = correct_text(transcription)

        out = find_in_text(transcription_updated, output_audio_f, to_find)
        print(transcription_updated)
        print(out)

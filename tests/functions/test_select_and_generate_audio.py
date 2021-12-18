from unittest import TestCase

from functions.select_and_generate_audio import select_and_generate_audio


class Test(TestCase):
    def test_select_and_generate_audio(self):
        folder = '/home/eb/Videos/arf/'
        file_input = 'test_input.mp4'
        file_output = 'test_output.mp4'

        out = select_and_generate_audio(folder, file_input, file_output)
        print(out)

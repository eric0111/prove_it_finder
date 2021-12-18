from unittest import TestCase
from functions.tokenize_video.tokenize_video import tokenize_video
from functions.tokenize_video.video_token import VideoToken


class Test(TestCase):
    def test_tokenize_video(self):
        folder = '/home/eb/Videos/arf/'
        file_input = 'input.mp4'

        video_tokens : [VideoToken] = tokenize_video(folder+file_input)
        for video_token in video_tokens:
            print(video_token.ss, video_token.to)

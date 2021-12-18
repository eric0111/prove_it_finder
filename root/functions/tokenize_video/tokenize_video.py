from functions.tokenize_video.utils import get_video_duration, convert_s_to_timestamp
from functions.tokenize_video.video_token import VideoToken


def tokenize_video(file_name, secs):
    duration = get_video_duration(file_name)

    i = 0
    window = secs  

    video_tokens = []
    while i < (duration - window):
        ss = convert_s_to_timestamp(i)
        to = convert_s_to_timestamp(i + window)
        video_tokens.append(VideoToken(ss, to))
        i += window

    return video_tokens


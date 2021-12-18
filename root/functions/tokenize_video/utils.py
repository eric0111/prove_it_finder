def get_video_duration(file_name):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(file_name)
    duration = float(clip.duration)
    return duration


def convert_s_to_timestamp(duration):
    import time
    return time.strftime("%H:%M:%S", time.gmtime(duration))
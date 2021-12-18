import os
from functions.tokenize_video.video_token import VideoToken

# cmd = 'ffmpeg -ss 00:00:00 -i /home/eb/Videos/arf/input.mp4 -to 00:30:00 /home/eb/Videos/arf/test_input.mp4'
# cmd = 'ffmpeg -ss 00:00:00 -i /home/eb/Videos/arf/input.mp4 -to 00:00:30 -c copy /home/eb/Videos/arf/test_input.mp4'


def trim_video(folder, input_video_f, output_video_f, video_token : VideoToken):
    ss = video_token.ss
    to = video_token.to

    cmd = 'ffmpeg -y -ss '+ss+' -i ' + folder+input_video_f + ' -to '+ to +' -c copy ' + folder+output_video_f
    os.system(cmd)



#trim_video()

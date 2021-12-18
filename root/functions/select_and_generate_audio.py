from functions.tokenize_video.video_token import VideoToken


def select_and_generate_audio(folder, file_input, file_output, video_token:VideoToken, os):
    fun_name = 'select_and_generate_audio'
    print(fun_name + ' started')

    #ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac
    output_audio_f = folder + file_output.split('.')[0] + '.wav'
    cmd = 'ffmpeg -y -nostats -loglevel panic -i ' + folder + file_input +' -ss '+ video_token.ss + ' -to '+ video_token.to+' ' + output_audio_f
    os.system(cmd)

    print(fun_name + ' finished')

    return output_audio_f


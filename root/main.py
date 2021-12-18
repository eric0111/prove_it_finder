import language_tool_python
from IPython.display import Audio
from functions.correct_text import correct_text
from functions.find_prove_it.find_prove_it import find_prove_it
from functions.generate_transcription import generate_transcription
from functions.select_and_generate_audio import select_and_generate_audio
from functions.tokenize_video.tokenize_video import tokenize_video
from functions.tokenize_video.video_token import VideoToken
import os

check_tool = language_tool_python.LanguageTool('en-US')

if __name__ == '__main__':
    #folder = '/home/eb/Videos/arf/'
    folder = '/Users/eb/Movies/arf/'
    file_input = 'input.mp4'
    file_output_temp = 'temp_output.mp4'
    to_find = 'set'
    secs = 45 ## secs

    video_tokens: [VideoToken] = tokenize_video(folder + file_input, secs)

    found_log = ''
    final_text = ''

    for video_token in video_tokens:
        output_audio_f = select_and_generate_audio(folder, file_input, file_output_temp, video_token, os)
        Audio(output_audio_f)

        transcription = generate_transcription(output_audio_f)

        transcription_updated = correct_text(transcription, check_tool)
        print(transcription_updated)
        final_text += transcription_updated

        found = find_prove_it(transcription_updated, output_audio_f, to_find, video_token)

        if len(found) > 0:
            found_log += str(found) + ' => ' + str(video_token.ss) + '\n'
            print(found, transcription_updated)
            #print(out, file=open(folder + 'log.txt', 'w'))
        #print(found, video_token.ss)

    print(found_log, file=open(folder + 'found_log.txt', 'w'))
    print(final_text, file=open(folder + 'final_text.txt', 'w'))

from IPython.display import Audio
from functions.correct_text import correct_text
from functions.find_in_text.find_in_text import find_in_text
from functions.generate_transcription import generate_transcription
from functions.select_and_generate_audio import select_and_generate_audio
from functions.tokenize_video.tokenize_video import tokenize_video
from functions.tokenize_video.video_token import VideoToken


def finder(file_input, folder, secs,  to_find, CHECK_TOOL, TOKENIZER,MODEL, os):
    video_tokens: [VideoToken] = tokenize_video(folder + file_input, secs)

    found_log = ''
    raw_text = ''
    final_text = ''

    for video_token in video_tokens:
        output_audio_f = select_and_generate_audio(folder, file_input, video_token, os)
        Audio(output_audio_f)

        transcription = generate_transcription(output_audio_f, TOKENIZER, MODEL)
        raw_text += transcription

        transcription_updated = correct_text(transcription, CHECK_TOOL)
        print(transcription_updated)
        final_text += transcription_updated

        found = find_in_text(transcription_updated, output_audio_f, to_find, video_token)

        if len(found) > 0:
            found_log += str(found) + ' => ' + str(video_token.ss) + '\n'
            print(found, transcription_updated)
            # print(out, file=open(folder + 'log.txt', 'w'))
        # print(found, video_token.ss)

    print(found_log, file=open(folder + file_input + 'raw_text.txt', 'w'))
    print(final_text, file=open(folder + file_input + 'final_text.txt', 'w'))
    print(found_log, file=open(folder + file_input + 'found_log.txt', 'w'))
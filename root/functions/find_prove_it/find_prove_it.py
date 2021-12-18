import re
import datetime

from functions.find_prove_it.utils import get_sec
from functions.let_at_sec import generate_letters_at_sec
from functions.tokenize_video.video_token import VideoToken


def find_prove_it(transcription, file_name, to_find, video_token : VideoToken):
    transcription = transcription.lower()

    ll = []
    let_at_sec = generate_letters_at_sec(file_name, transcription)

    for m in re.finditer(to_find, transcription):
        num = m.start()
        ll.append('position: ' + str(num))
        secs = int(num / let_at_sec) + get_sec(video_token.ss)
        #ll.append('secs: ' + str(secs))
        conversion = datetime.timedelta(seconds=secs)
        ll.append('timestamp: ' + str(conversion))

    return ll

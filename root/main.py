import os
from finder import finder
import language_tool_python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

CHECK_TOOL = language_tool_python.LanguageTool('en-US')
TOKENIZER = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
MODEL = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

if __name__ == '__main__':
    #folder = '/home/eb/Videos/arf/'
    folder = '/Users/eb/Movies/arf/downloads/'
    to_find = 'prove'
    secs = 45 ## token secs

    files = os.listdir(folder)
    for file in files:
        print('######################\n', file, '\n######################')
        finder(file, folder, secs, to_find, CHECK_TOOL, TOKENIZER,MODEL, os)



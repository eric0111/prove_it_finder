import language_tool_python


def correct_text(transcription):
    fun_name = 'correct_text'
    print(fun_name + ' started')

    tool = language_tool_python.LanguageTool('en-US')

    print(fun_name + ' finished')
    return tool.correct(transcription)

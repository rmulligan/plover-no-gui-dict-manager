import os

def inline_lookup_chord(translator, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()

    # Append the word to the file
    with open(os.path.expanduser('/root/.config/plover/fingerspelled_words.log'), 'a') as f:
        f.write(last_word + '\n')

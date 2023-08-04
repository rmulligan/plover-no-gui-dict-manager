from plover_gtm.plugin import PloverGtmPlugin

import os

def inline_lookup_chord(engine, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()
    if last_word:
        with open(os.path.expanduser("~/.config/plover/typed_words.log"), 'a') as log_file:
            log_file.write(last_word + '\n')

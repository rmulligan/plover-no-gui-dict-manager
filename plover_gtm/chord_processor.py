from plover import log
from plover_gtm.plugin import PloverGtmPlugin

def inline_lookup_chord(translator, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()

    # Get all dictionaries from the translator
    all_dictionaries = translator.get_dictionary()

    steno_strokes_list = all_dictionaries.reverse_lookup(last_word)

    if not steno_strokes_list:
        log.info("No steno strokes found for word '{}'".format(last_word))
    else:
        shortest_steno_strokes = min(steno_strokes_list, key=len)
        log.info("Shortest steno strokes for word '{}': {}".format(last_word, shortest_steno_strokes))

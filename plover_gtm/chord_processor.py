from plover import log
from plover_gtm.plugin import PloverGtmPlugin

def inline_lookup_chord(translator, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()

    # Get all dictionaries from the translator
    all_dictionaries = translator.get_all_dictionaries()

    for dictionary in all_dictionaries:
        steno_strokes_list = dictionary.reverse_lookup(last_word)

        if not steno_strokes_list:
            log.info(f"No steno strokes found for word '{last_word}' in dictionary {dictionary}")
        else:
            shortest_steno_strokes = min(steno_strokes_list, key=len)
            log.info(f"Shortest steno strokes for word '{last_word}': {shortest_steno_strokes}")

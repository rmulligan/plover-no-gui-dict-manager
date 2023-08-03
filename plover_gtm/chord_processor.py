from plover import log
from plover_gtm.plugin import PloverGtmPlugin

def inline_lookup_chord(translator, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()

    # Get all steno strokes for the last word
    steno_strokes_list = get_all_strokes(translator, last_word)

    if not steno_strokes_list:
        log.info("No steno strokes found for word '{}'".format(last_word))
    else:
        shortest_steno_strokes = min(steno_strokes_list, key=len)
        log.info("Shortest steno strokes for word '{}': {}".format(last_word, shortest_steno_strokes))

def get_all_strokes(translator, word):
    # Use the lookup function to get all steno strokes for the word
    all_strokes = translator.get_dictionary().lookup(word)

    # Filter out any None values (these are returned when the word is not found in a dictionary)
    all_strokes = [strokes for strokes in all_strokes if strokes is not None]

    # Return the list of all steno strokes
    return all_strokes

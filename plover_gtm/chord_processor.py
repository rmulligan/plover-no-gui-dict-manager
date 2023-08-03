from plover import log
# from plover_gtm.plugin import gtm

def inline_lookup_chord(translator, _stroke, _):
    last_word = 'Testing'
    steno_strokes_list = translator.get_dictionary().casereverse_lookup(last_word)

    if not steno_strokes_list:
        log.info("No steno strokes found for word '{}'".format(last_word))
    else:
        shortest_steno_strokes = min(steno_strokes_list, key=len)
        log.info("Shortest steno strokes for word '{}': {}".format(last_word, shortest_steno_strokes))

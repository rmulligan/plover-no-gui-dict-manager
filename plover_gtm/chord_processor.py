from plover.engine import Translator
from plover.steno import Stroke

def lookup_chord(translator, _stroke, _):
    last_word = translator.get_last_translation().english.lower()
    steno_strokes_list = translator.get_dictionary().casereverse_lookup(last_word)

    if not steno_strokes_list:
        return "No steno strokes found for word '{}'".format(last_word)

    shortest_steno_strokes = min(steno_strokes_list, key=len)

    return "Shortest steno strokes for word '{}': {}".format(last_word, shortest_steno_strokes)

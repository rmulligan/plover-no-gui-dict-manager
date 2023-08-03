from plover.engine import Translator
from plover.steno import Stroke
from plover.translation import Translation

def lookup_chord(translator, _stroke, _):
    buffer = translator.get_state().buffer
    if len(buffer) > 0 and isinstance(buffer[-1], Translation):
        last_translation = buffer[-1].english.lower()
    else:
        last_translation = ""

    steno_strokes_list = translator.get_dictionary().casereverse_lookup(last_translation)

    if not steno_strokes_list:
        return "No steno strokes found for word '{}'".format(last_translation)

    shortest_steno_strokes = min(steno_strokes_list, key=len)

    return "Shortest steno strokes for word '{}': {}".format(last_translation, shortest_steno_strokes)

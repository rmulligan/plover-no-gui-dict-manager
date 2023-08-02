"""
This module provides a Plover command for processing chords.
When a specific chord is entered, it attempts to replace the last
fingerspelled word with its steno equivalent. If the word is not in
the user's dictionary, it prompts the user to enter a new chord for
that word.
"""
from plover.engine import StenoEngine
from plover.formatting import RetroFormatter
import plover.log as log

def looksert(engine: StenoEngine, _arg: str):
    # Create a RetroFormatter instance with the previous translations from the engine
    formatter = RetroFormatter(engine.translator_state.translations)

    # Get the last word from the buffer
    last_word = formatter.last_words(1)[0]

    # Reverse lookup the word to get the steno strokes
    steno_strokes_list = engine.reverse_lookup(last_word)

    # Log all the steno strokes that map to the word
    for steno_strokes in steno_strokes_list:
        log.info("Steno strokes for word {}: {}".format(last_word, steno_strokes))

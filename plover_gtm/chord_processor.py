"""
This module provides a Plover command for processing chords.
When a specific chord is entered, it attempts to replace the last
fingerspelled word with its steno equivalent. If the word is not in
the user's dictionary, it prompts the user to enter a new chord for
that word.
"""
from plover.engine import StenoEngine
import plover.log as log

def looksert(engine: StenoEngine, _arg: str):
    # Get the last word from the buffer
    last_word = engine.translator_state[-1].english[0]

    # Perform the lookup
    chord = engine.lookup((last_word,))

    if chord:
        # Log the chord if it was found in the dictionary
        log.info("Found chord for word {}: {}".format(last_word, chord))
    else:
        # If the chord is not found, log a message indicating this
        log.info("No chord found for word {}".format(last_word))

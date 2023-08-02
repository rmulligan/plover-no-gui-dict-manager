"""
This module provides a Plover command for processing chords.
When a specific chord is entered, it attempts to replace the last
fingerspelled word with its steno equivalent. If the word is not in
the user's dictionary, it prompts the user to enter a new chord for
that word.
"""
from plover.engine import StenoEngine
from plover.formatting import RetroFormatter
from plover.output import Output
import plover.log as log

def looksert(engine: StenoEngine, _arg: str):
    # Create a RetroFormatter instance with the previous translations from the engine
    formatter = RetroFormatter(engine.translator_state.translations)

    # Get the last word from the buffer
    last_word = formatter.last_words(1)[0]

    # Reverse lookup the word to get the steno strokes
    steno_strokes_list = engine.casereverse_lookup(last_word)

    # If there are no steno strokes for this word, there's nothing more to do
    if not steno_strokes_list:
        log.info(f"No steno strokes found for word '{last_word}'")
        return

    # Find the shortest steno stroke
    shortest_steno_strokes = min(steno_strokes_list, key=len)

    # Log the shortest steno strokes for the word
    log.info(f"Shortest steno strokes for word '{last_word}': {shortest_steno_strokes}")

    # Create an instance of Output
    output = Output()

    # Erase the last word
    output.send_backspaces(len(last_word))

    # Output the shortest steno strokes
    output.send_string('/'.join(shortest_steno_strokes))

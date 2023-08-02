"""
This module provides a Plover command for processing chords.
When a specific chord is entered, it attempts to replace the last
fingerspelled word with its steno equivalent. If the word is not in
the user's dictionary, it prompts the user to enter a new chord for
that word.
"""
from plover.formatting import Formatter, RetroFormatter, _Action
from plover.engine import StenoEngine
import plover.log as log
from plover.steno import Stroke

def looksert(engine: StenoEngine, _arg: str):
    log.info("looksert command called")

    # Create a RetroFormatter instance with the previous translations from the engine
    retro_formatter = RetroFormatter(engine.translator_state.translations)

    # Get the last word from the buffer
    last_word = retro_formatter.last_words(1)[0]

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

    # Create a new action that replaces the last word with the shortest steno strokes
    action = _Action(prev_replace=last_word, text=' '.join(shortest_steno_strokes))

    retro_formatter.format([], [action], action)

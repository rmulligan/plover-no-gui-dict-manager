"""
This module provides a Plover command for processing chords.
When a specific chord is entered, it attempts to replace the last
fingerspelled word with its steno equivalent. If the word is not in
the user's dictionary, it prompts the user to enter a new chord for
that word.
"""

from plover.formatting import RetroFormatter
import plover.log

def looksert(engine, _argument):
    retro_formatter = RetroFormatter(engine.translator_state.prev())
    last_word = retro_formatter.last_words(count=1)
    plover.log.info("Last word: " + str(last_word))

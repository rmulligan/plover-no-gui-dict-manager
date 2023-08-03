from plover.formatting import _Action
from plover.steno import Stroke
from plover.formatting import RetroFormatter

def stroke_to_steno_string(stroke: Stroke) -> str:
    """Converts a steno stroke to a string representation."""
    keys = stroke.steno_keys
    if keys is None:
        return ''
    steno_string = ''.join(keys)
    if stroke.is_number:
        steno_string += '#'
    return steno_string

def looksert(ctx, _arg: str):
    # Create a RetroFormatter instance with the previous translations from the context
    retro_formatter = RetroFormatter(ctx.output)

    # Get the last word from the buffer
    last_word = retro_formatter.last_words(1)[0]

    # Get the last stroke from the buffer
    last_stroke = retro_formatter.last_strokes(1)[0]

    # Convert the steno stroke to a string
    steno_string = stroke_to_steno_string(last_stroke)

    # Create a new action that replaces the last word with the steno string
    action = _Action(prev_replace=last_word, text=steno_string)

    return action

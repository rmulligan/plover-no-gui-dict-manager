from plover.formatting import _Action
from plover.steno import Stroke

class LastWordTracker:
    def __init__(self):
        self.last_word = None

    def on_translated(self, _old: _Action, new: _Action):
        if new is not None and new.english is not None:
            self.last_word = new.english

    def get_last_word(self):
        return self.last_word

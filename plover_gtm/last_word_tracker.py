from plover.formatting import _Action
from plover.steno import Stroke

class LastWordTracker:
    def __init__(self):
        self.last_word = None
        self.fingerspelling_buffer = ""
        self.single_char_count = 0

    def on_translated(self, _old: _Action, new: _Action):
        if new is not None and new.text is not None:
            if len(new.text) == 1:
                # this is a single character, could be a fingerspelled letter
                self.fingerspelling_buffer += new.text
                self.single_char_count += 1
                if self.single_char_count >= 3:
                    # we have seen at least 3 single characters in a row, consider it as a word
                    self.last_word = self.fingerspelling_buffer
            else:
                # this is a whole word (or a command), so if there's any word in the buffer, save it
                if self.single_char_count >= 3:
                    self.last_word = self.fingerspelling_buffer
                else:
                    self.last_word = new.text
                # reset the buffer and single character counter
                self.fingerspelling_buffer = ""
                self.single_char_count = 0

    def get_last_word(self):
        # if there's a word in the buffer, return it, otherwise return the last whole word
        return self.fingerspelling_buffer if self.fingerspelling_buffer else self.last_word

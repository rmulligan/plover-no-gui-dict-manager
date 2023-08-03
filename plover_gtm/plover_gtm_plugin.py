from plover.engine import StenoEngine
from .last_word_tracker import LastWordTracker

class PloverGtmPlugin:
    def __init__(self, engine: StenoEngine):
        self.engine = engine
        self.last_word_tracker = LastWordTracker()

    def start(self):
        self.engine.hook_connect("translated", self.last_word_tracker.on_translated)

from plover.engine import StenoEngine
from .last_word_tracker import LastWordTracker
from plover import log

class PloverGtmPlugin:
    def __init__(self, engine: StenoEngine):
        log.info('PloverGtmPlugin __init__ called')
        self.engine = engine
        self.last_word_tracker = LastWordTracker()

    def start(self):
        log.info('PloverGtmPlugin start called')
        self.engine.hook_connect("translated", self.last_word_tracker.on_translated)

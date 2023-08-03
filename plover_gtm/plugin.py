from plover.engine import StenoEngine
from .last_word_tracker import LastWordTracker
from plover import log

class PloverGtmPlugin:
    def __init__(self, engine: StenoEngine):
        log.info("PloverGtmPlugin: __init__")
        self._engine = engine
        self._last_word_tracker = LastWordTracker()

    def start(self):
        log.info("PloverGtmPlugin: start")
        self._engine.hook_connect("translated", self.on_translation_added)

    def stop(self):
        log.info("PloverGtmPlugin: stop")

        self._engine.hook_disconnect("translated", self.on_translation_added)

    def on_translation_added(self, old, new):
        log.info("PloverGtmPlugin: on_translation_added")
        self._last_word_tracker.on_translated(old, new)

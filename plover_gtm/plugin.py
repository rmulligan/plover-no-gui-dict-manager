from plover.engine import StenoEngine
from .last_word_tracker import LastWordTracker
from plover import log

class PloverGtmPlugin:
    _instance = None

    @classmethod
    def get_instance(cls, engine=None):
        if cls._instance is None:
            if engine is None:
                raise ValueError("Engine must be provided when creating the first instance")
            cls._instance = cls(engine)
        return cls._instance

    @classmethod
    def set_instance(cls, instance):
        cls._instance = instance

    def __init__(self, engine: StenoEngine):
        if self._instance is not None:
            raise ValueError("An instance of PloverGtmPlugin already exists")
        self._engine = engine
        log.info("PloverGtmPlugin: __init__")
        self._last_word_tracker = LastWordTracker()

    def start(self):
        log.info("PloverGtmPlugin: start")
        self._engine.hook_connect("translated", self.on_translation_added)

    def stop(self):
        log.info("PloverGtmPlugin: stop")

        self._engine.hook_disconnect("translated", self.on_translation_added)

    def on_translation_added(self, old, new):
        log.info("PloverGtmPlugin: on_translation_added triggered")
        if new:
            self._last_word_tracker.on_translated(old[-1] if old else None, new[-1])

    def get_last_word(self):
        return self._last_word_tracker.get_last_word()

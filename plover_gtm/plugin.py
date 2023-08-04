from plover.engine import StenoEngine
from plover import log
import os

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
        return cls._instance

    def __init__(self, engine: StenoEngine):
        if self._instance is not None:
            raise ValueError("An instance of PloverGtmPlugin already exists")
        self._engine = engine
        log.info("PloverGtmPlugin: __init__")
        self._capturing = False
        self._capture_buffer = []

    def start(self):
        log.info("PloverGtmPlugin: start")
        self._engine.hook_connect("translated", self.on_translation_added)

    def stop(self):
        log.info("PloverGtmPlugin: stop")
        self._engine.hook_disconnect("translated", self.on_translation_added)

    def on_translation_added(self, old, new):
        log.info("PloverGtmPlugin: on_translation_added triggered")
        if new and self._capturing:
            self._capture_buffer.append(new[-1].text)

    def start_capture(self):
        log.info("PloverGtmPlugin: start_capture")
        self._capturing = True
        self._capture_buffer = []

    def end_capture(self):
        log.info("PloverGtmPlugin: end_capture")
        with open(os.path.expanduser("~/.config/plover/typed_words.log"), "a") as f:
            f.write("".join(self._capture_buffer))  # Join the words with spaces
            f.write("\n")  # Write a newline character after each capture session
        self._capturing = False
        self._capture_buffer = []

    def abort_capture(self):
        log.info("PloverGtmPlugin: abort_capture")
        self._capturing = False
        self._capture_buffer = []

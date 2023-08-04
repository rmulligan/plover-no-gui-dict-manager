from plover import log
from plover.formatting import _Action
from plover_gtm.plugin import PloverGtmPlugin

def start_capture(engine, stroke, command):
    PloverGtmPlugin.get_instance().start_capture()
    return _Action()

def end_capture(engine, stroke, command):
    PloverGtmPlugin.get_instance().end_capture()
    return _Action()

def abort_capture(engine, stroke, command):
    PloverGtmPlugin.get_instance().abort_capture()
    return _Action()

def capture_word(engine, stroke, command):
    PloverGtmPlugin.get_instance().capture_word(command)
    return _Action()

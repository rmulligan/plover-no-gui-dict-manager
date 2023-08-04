from plover import log
from plover_gtm.plugin import PloverGtmPlugin

def start_capture(engine, stroke, command):
    log.info("start_capture")
#    PloverGtmPlugin.get_instance().start_capture()

def end_capture(engine, stroke, command):
    log.info("end_capture")
#    PloverGtmPlugin.get_instance().end_capture()

def abort_capture(engine, stroke, command):
    # log.info("abort_capture")
    PloverGtmPlugin.get_instance().abort_capture()

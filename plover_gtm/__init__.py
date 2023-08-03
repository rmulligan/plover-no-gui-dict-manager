from plover.engine import StenoEngine
from .plugin import PloverGtmPlugin
from plover import log

def setup(engine: StenoEngine):
    log.info("Setup called")
    PloverGtmPlugin.set_instance(PloverGtmPlugin(engine))

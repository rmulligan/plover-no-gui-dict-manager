from plover.engine import StenoEngine
from .plugin import PloverGtmPlugin

def setup(engine: StenoEngine):
    log.info("Setup called")
    return PloverGtmPlugin(engine)

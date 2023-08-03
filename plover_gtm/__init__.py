from plover.engine import StenoEngine
from .plugin import PloverGtmPlugin

def setup(engine: StenoEngine):
    return PloverGtmPlugin(engine)

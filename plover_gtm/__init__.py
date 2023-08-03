from plover.engine import StenoEngine
from .plugin import PloverGtmPlugin

gtm = PloverGtmPlugin(StenoEngine())
gtm.start()

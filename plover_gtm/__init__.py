from .plugin import get_instance

def start_plugin(engine):
    plugin_instance = get_instance()
    plugin_instance.start()

def stop_plugin(engine):
    pass  # Add any necessary cleanup code here

from plover import log
from plover.formatting import _Action
from plover_gtm.plugin import PloverGtmPlugin

def inline_lookup_chord(translator, _stroke, _):
    last_word = PloverGtmPlugin.get_instance().get_last_word()
    all_dictionaries = translator.get_dictionary()
    steno_strokes_list = all_dictionaries.reverse_lookup(last_word)

    if not steno_strokes_list:
        log.info("No steno strokes found for word '{}'".format(last_word))
    else:
        shortest_steno_strokes = min(steno_strokes_list, key=len)
        log.info("Shortest steno strokes for word '{}': {}".format(last_word, shortest_steno_strokes))

        # Send backspaces to delete the last word
        backspaces = len(last_word)
        backspace_action = _Action(text='*' * backspaces)
        translator.translate_action(backspace_action)

        # Send the brief
        brief = '/' + '/'.join(shortest_steno_strokes) + '/'
        brief_action = _Action(text=brief)
        translator.translate_action(brief_action)

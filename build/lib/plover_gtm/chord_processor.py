import plover.steno_dictionary

class ChordProcessingCommand:

    def __init__(self):
        self.user_dict = plover.steno_dictionary.StenoDictionary()
        self.user_dict.load('user.json')

    def lookup(self, word):
        # Implement lookup logic here

    def add_to_dictionary(self, word, chord):
        # Implement addition to dictionary logic here

    def check_conflict(self, chord):
        # Implement conflict check logic here

    def execute(self, chord):
        # Main logic of the command:
        # 1. Detect the specific chord
        # 2. Look up the word in the dictionaries
        # 3. If the word exists, replace it with the raw steno and highlight
        # 4. If the word does not exist, replace the word with 'ENTER CHORD' and highlight
        # 5. Capture the raw strokes
        # 6. If no conflict, add the chord to the user.json dictionary, replace 'ENTER CHORD' with new raw steno, and highlight
        # 7. If there is a conflict, replace 'ENTER CHORD' with 'CONFLICT' and highlight, waiting for the next entry
        # 8. Escape plugin if 'esc' is entered

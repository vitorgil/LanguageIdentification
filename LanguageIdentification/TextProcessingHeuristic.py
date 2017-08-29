
class TextProcessingHeuristic(object):
    """Base class for text processing heuristics"""
    
    def ProcessText(self, text):
        # The only heuristic that's applied to all texts is making all chars low.
        # But even the amount of capital letters compared with the rest of the text 
        # could count for idetifying the language. Like, maybe some languages have 
        # longer sentences and so less capital letters comparatively?
        return text.lower()


def char_range(c1, c2) -> list:
    """Generates the characters from `c1` to `c2`, inclusive."""
    _range = list()
    for c in range(ord(c1), ord(c2)+1):
        _range.append(chr(c))
    return _range

class OnlyAToZ(TextProcessingHeuristic):
     """Eliminates all characters which are not in the range a to z"""

     def __init__(self):
        self.allowedCharaters = char_range('a', 'z')

     def ProcessText(self, text):
        text = super().ProcessText(text)
        text = ''.join(c for c in text if c in self.allowedCharaters)
        return text

class LetAllCharsPass(TextProcessingHeuristic):
    """Let's all characters pass except punctuation, spaces, etc."""

    def __init__(self):
        self.allowedCharaters = char_range('a', 'z')
        for i in range(128, 155):
            self.allowedCharaters.append(chr(i))
        for i in range(160, 165):
            self.allowedCharaters.append(chr(i))
        for i in range(224, 237):
            self.allowedCharaters.append(chr(i))

    def ProcessText(self, text):
        text = super().ProcessText(text)
        text = ''.join(c for c in text if c in self.allowedCharaters)
        return text

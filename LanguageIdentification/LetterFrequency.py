from collections import namedtuple

class LetterFrequency:
    """container for a letter and its frequency (with)in a (con)text"""

    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency

    def __eq__(self, other):
        return self.char == other.char

    def __gt__(self, other):
        return self.char > other.char

    def GetFrequency(self):
        return self.frequency

class LetterFrequencies:
    """container for several LetterFrequencies"""
    
    def __init__(self, text=""):
        self.frequenciesPerLanguage = list()
        
        if text == "":
            return

        # count chars and create frequencies
        lettersAndCount = dict()
        letterCount = 0
        for char in text:
            lettersAndCount[char] = lettersAndCount.get(char, 0) + 1
            letterCount += 1

        for char in lettersAndCount:
            self.frequenciesPerLanguage.append(LetterFrequency(char, lettersAndCount[char] / letterCount))

    def AddFromStatistic(self, frequenciesForLanguage):
        self.frequenciesPerLanguage.append(frequenciesForLanguage)

    def Sort(self):
        self.frequenciesPerLanguage.sort()

    def GetCharsWithHighestFrequency(self, count):
        localList = list(self.frequenciesPerLanguage)
        localList.sort(key=LetterFrequency.GetFrequency, reverse=True)
        return localList[0:count-1]
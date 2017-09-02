from collections import namedtuple

class LetterFrequency:
    """container for a char and its count and frequency (with)in a (con)text"""

    def __init__(self, char, freqency=0.0):
        self.char = char
        self.count = 0
        self.frequency = freqency

    def __eq__(self, other):
        return self.char == other.char

    def __gt__(self, other):
        return self.char > other.char

    def GetFrequency(self):
        return self.frequency

class LetterFrequencies:
    """container for several LetterFrequencies"""
    
    def __init__(self, text=""):
        self.frequencies = list()
        
        # count chars and create frequencies
        lettersAndCount = dict()
        for char in text:
            lettersAndCount[char] = lettersAndCount.get(char, 0) + 1
            
            self.CharFound(char)

        #totalCount = 0
        #for char in lettersAndCount:
        #    totalCount += lettersAndCount[char]
        
        #for char in lettersAndCount:
        #    self.frequencies.append(LetterFrequency(char, lettersAndCount[char] / totalCount))

    def CharFound(self, char):
        # create occurrence object and add it if it doesn't exist
        occurrence = LetterFrequency(char)
        if occurrence not in self.frequencies:
            self.frequencies.append(occurrence)
        
        # now increase the count of the new (or already existing) element
        self.frequencies[self.frequencies.index(occurrence)].count += 1

    def AddFromStatistic(self, occurrence):
        self.frequencies.append(occurrence)

    def Sort(self):
        self.frequencies.sort()

    def CalculateFrequencies(self):
        totalCount = self.GetTotalCount()
        for letterFrequency in self.frequencies:
            letterFrequency.frequency = letterFrequency.count / totalCount

    def GetTotalCount(self):
        totalCount = 0
        for letterFrequency in self.frequencies:
            totalCount += letterFrequency.count
        return totalCount

    def GetCharsWithHighestFrequency(self, count):
        localList = list(self.frequencies)
        localList.sort(key=LetterFrequency.GetFrequency, reverse=True)
        return localList[0:count-1]
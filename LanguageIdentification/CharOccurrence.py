
class CharCount:
    """container for a char and its count and frequency (with)in a (con)text"""
    char = ''
    count = 0
    frequency = float(0.0)

    def __init__(self, char):
        self.char = char

    def __eq__(self, other):
        return self.char == other.char

    def __gt__(self, other):
        return self.char > other.char

class CharCounts:
    """container for several CharCounts"""
    
    def __init__(self, text=""):
        self.occurrences = list()
        for char in text:
            self.CharFound(char)

    def CharFound(self, char):
        # create occurrence object and add it if it doesn't exist
        occurrence = CharCount(char)
        if occurrence not in self.occurrences:
            self.occurrences.append(occurrence)
        
        # now increaese the count of the new (or already existing) element
        self.occurrences[self.occurrences.index(occurrence)].count += 1

    def AddOccurrenceFromStatistic(self, occurrence):
        self.occurrences.append(occurrence)

    def Sort(self):
        self.occurrences.sort()

    def CalculateFrequencies(self):
        totalCount = self.GetTotalCount()
        for charOccurrence in self.occurrences:
            charOccurrence.frequency = charOccurrence.count / totalCount

    def GetTotalCount(self):
        totalCount = 0
        for charOccurrence in self.occurrences:
            totalCount += charOccurrence.count
        return totalCount

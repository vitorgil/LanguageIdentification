from CharOccurrence import *
from FrequenciesLoader import *
from TextProcessingHeuristic import *
from os import listdir
from os.path import isfile, join
from collections import namedtuple

def ProcessText(fileName) -> CharCounts:
    # read file content
    file = open(fileName, "r")
    fileContent = file.read()
    
    # apply heuristics for text processing
    heuristic = OnlyAToZ()
    fileContent = heuristic.ProcessText(fileContent)
    
    # create CharCounts object
    charCounts = CharCounts(fileContent)

    charCounts.Sort()
    charCounts.CalculateFrequencies()
    return charCounts


def getKey(item):
    return item[1]


def GetBestMatch(occurrences, frequencies) -> Languages:
    """Takes char occurrences in a text and a "list of lists": the frequencies per language, per character"""
    
    DiffPerLanguage = namedtuple('DiffPerLanguage', 'diff language')

    heuristicValues = list()

    for frequencyForLanguage in frequencies:
        freqDiffSum = 0
        for occurrence in occurrences.occurrences:
            if occurrence in frequencyForLanguage[1].occurrences:
                # Only check chars for which a frequency is known
                charOccurrence = frequencyForLanguage[1].occurrences[frequencyForLanguage[1].occurrences.index(occurrence)]
                freqDiffSquared = pow(abs(charOccurrence.frequency - occurrence.frequency), 2)
                freqDiffSum += freqDiffSquared

        heuristicValues.append(DiffPerLanguage(freqDiffSum, frequencyForLanguage[0].name))

    for value in heuristicValues:
        print(value.language + ": " + str(value.diff))
    print()

    heuristicValues.sort(key=getKey)
    bestMatch = heuristicValues[0]
    for item in heuristicValues:
        if item.diff < bestMatch.diff:
            bestMatch = item

    return bestMatch.language

class LanguageIdentificationTester():
    """description of class"""

    def Test(self):
        self.frequencies = FrequenciesLoader.Load()
        self.TestLanguage(Languages.English)
        self.TestLanguage(Languages.Portuguese)
        self.TestLanguage(Languages.Italian)
        self.TestLanguage(Languages.Dutch)
        self.TestLanguage(Languages.Spanish)

    def TestLanguage(self, language):
        print('Testing ' + language.name)
        path = "Resources\\" + language.name
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in onlyfiles:
            occurrences = ProcessText(path + "\\" + file)        
            bestMatch = GetBestMatch(occurrences, self.frequencies)
            print(file + "  -> " + bestMatch)

        print()

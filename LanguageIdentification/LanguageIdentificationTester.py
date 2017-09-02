from LetterFrequency import *
from FrequenciesLoader import *
from TextProcessingHeuristic import *
from os import listdir
from os.path import isfile, join
from collections import namedtuple

def ProcessText(fileName, processingHeuristic) -> LetterFrequencies:
    """Reads a file, processes it according to a desired heuristic and returns 
    letter frequency after processing."""

    # read file content
    file = open(fileName, "r")
    fileContent = file.read()
    
    # apply heuristics for text processing
    fileContent = processingHeuristic.ProcessText(fileContent)
    
    # create LetterFrequencies object
    letterFrequencies = LetterFrequencies(fileContent)

    # Sort the list by letter and calculate frequencies
    letterFrequencies.Sort()
    
    return letterFrequencies

def GetBestMatch(textFrequencies, frequencies) -> Languages:
    """Takes letter frequencies in a text and a "list of lists": the frequencies per language, per character"""
    
    DiffPerLanguage = namedtuple('DiffPerLanguage', 'diff language')

    heuristicValues = list()

    for frequencyForLanguage in frequencies:
        highest = frequencyForLanguage[1].GetCharsWithHighestFrequency(10)
        freqDiffSum = 0
        for frequency in textFrequencies.frequenciesPerLanguage:
            if frequency in highest:
                # Only check chars for which a frequency is known
                letterFrequency = frequencyForLanguage[1].frequenciesPerLanguage[frequencyForLanguage[1].frequenciesPerLanguage.index(frequency)]
                freqDiffSquared = pow(abs(letterFrequency.frequency - frequency.frequency), 2)
                freqDiffSum += freqDiffSquared

        heuristicValues.append(DiffPerLanguage(freqDiffSum, frequencyForLanguage[0]))

    bestMatch = heuristicValues[0]
    for item in heuristicValues:
        if item.diff < bestMatch.diff:
            bestMatch = item

    return bestMatch.language

class LanguageIdentificationTester():
    """Tests language identification by looking at letter frequency in a text and 
    comparing that with standard known frequencies for a set languages"""

    # Heuristic to apply when reading in files
    readInHeuristic = OnlyAToZ()

    def Test(self):
        # Get letter frequencies per language
        self.frequenciesPerLanguage = FrequenciesLoader.Load()
        
        # Test desired languages
        self.TestLanguage(Languages.English)
        self.TestLanguage(Languages.Portuguese)
        self.TestLanguage(Languages.Italian)
        self.TestLanguage(Languages.Dutch)
        self.TestLanguage(Languages.Spanish)


    def TestLanguage(self, language):
        """Tests language identification for a language"""

        print('Testing ' + language.name)

        # Texts per language are in a known folder
        path = "Resources\\" + language.name
        
        # get all files in that folder
        files = [f for f in listdir(path) if isfile(join(path, f))]
        
        # test each of the files
        for file in files:
            # get letter frequency in the text
            frequenciesInText = ProcessText(path + "\\" + file, self.readInHeuristic)
            
            # get the best match for which language the text is written in
            bestMatch = GetBestMatch(frequenciesInText, self.frequenciesPerLanguage)
            
            # Is the best match the language the text is written in?
            isWellGuessed = bestMatch == language

            # print what the best match is
            print(file + " -> " + bestMatch.name)

        print()

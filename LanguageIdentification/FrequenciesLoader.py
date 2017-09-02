from LetterFrequency import LetterFrequencies, LetterFrequency
from sys import *
from TextProcessingHeuristic import *
from enum import Enum

class Languages(Enum):
    Dutch = 1
    English = 2
    Esperanto = 3
    French = 4
    German = 5
    Italian = 6
    Polish = 7
    Portuguese = 8
    Spanish = 9
    Swedish = 10
    Turkish = 11

class FrequenciesLoader(object):
    """Loads char frequencies for several languages"""

    @staticmethod
    def Load():
        """Creates a list of letter frequencies per language"""
        frequenciesPerLanguage = list()
        for language in Languages:
            frequenciesPerLanguage.append([language, FrequenciesLoader.LoadFrequency(language)])
        return frequenciesPerLanguage
    
    @staticmethod
    def LoadFrequency(language) -> LetterFrequencies:
        """Loads letter frequency for a language."""
        # Open the file with frequency values for language and read it.
        # The file contains one line per character, in the format:
        # a 3%
        # b 10%
        # ...
        file = open("resources\\Frequencies\\" + language.name + ".txt", "r", encoding="utf8")
        fileContent = file.readlines()

        frequencies = LetterFrequencies()
        for line in fileContent:
            columns = line.split()
            # Initialize a LetterFrequency with the character and its frequency...
            frequencies.AddFromStatistic(LetterFrequency(columns[0], float(columns[1].strip('%')) / 100))
    
        return frequencies

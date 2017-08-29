from CharOccurrence import CharCounts, CharCount
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
        frequencies = list()
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Dutch))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.English))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Esperanto))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.French))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.German))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Italian))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Polish))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Portuguese))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Spanish))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Swedish))
        frequencies.append(FrequenciesLoader.CreateFrequencyTuple(Languages.Turkish))
        return frequencies

    @staticmethod
    def CreateFrequencyTuple(language):
        return [language, FrequenciesLoader.LoadFrequency(language)]

    @staticmethod
    def LoadFrequency(language):
        file = open("resources\\Frequencies\\" + language.name + ".txt", "r", encoding="utf8")
        fileContent = file.readlines()

        occurrences = CharCounts()
        for line in fileContent:
            columns = line.split()
            occurrence = CharCount(columns[0])
            occurrence.frequency = float(columns[1].strip('%')) / 100
            occurrences.AddOccurrenceFromStatistic(occurrence)
    
        return occurrences

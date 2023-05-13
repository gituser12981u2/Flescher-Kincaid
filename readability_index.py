import textstat


class ReadabilityIndex:
    def __init__(self, name, description, calculation_function, additional_function=None):
        self.name = name
        self.description = description
        self.calculation_function = calculation_function
        self.additional_function = additional_function


READABILITY_INDICES = [
    ReadabilityIndex("Flesch-Kincaid",
                     "Flesch-Kincaid is a readability index that measures the grade level required to understand the text.",
                     textstat.flesch_kincaid_grade,  # type: ignore
                     textstat.flesch_reading_ease),  # type: ignore
    ReadabilityIndex("Gunning Fog index",
                     "Gunning Fog index estimates the years of formal education required to understand the text.",
                     textstat.gunning_fog),   # type: ignore
    ReadabilityIndex("SMOG",
                     "SMOG is a grade formula that measures the reading level based on the number of complex words in the text.",
                     textstat.smog_index),  # type: ignore
    ReadabilityIndex("Coleman-Liau Index",
                     "Coleman-Liau Index calculates the grade level based on characters per word and words per sentence.",
                     textstat.coleman_liau_index),  # type: ignore
    ReadabilityIndex("ARI",
                     "ARI (Automated Readability Index) provides the grade level required to understand the text.",
                     textstat.automated_readability_index)  # type: ignore
]

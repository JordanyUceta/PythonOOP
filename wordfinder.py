import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    def __init__(self, path): 
        """Read path and reports # items read
        
        >>> wf = WordFinder("simple.txt") 
        3 words read 

        >>> wf.random() 
        random word 

        """ 

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file): 
        """Read all the words from the list and return a list of words""" 

        return [w.strip() for w in dict_file] 

    def random(self): 
        """Here we grab a random word""" 

        return random.choice(self.words)

class SpecialWordFinder(WordFinder): 
    """Specialized wordfinder that exlides blank lines/comments. 

    >>> swf = SpecialWordFinder("complex.txt") 
    3 words read

    """

    def parse(self, dict_file): 
        """Get the file and return a list of words""" 

        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')] 
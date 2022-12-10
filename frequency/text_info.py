from frequency import letter_frequency as lf, utils, index_of_coincidence as ioc

class textInfo:
    __slots__ = ["__letter_count", "__total_letters","__total_length","__index_of_coincidence","__letter_frequency"]
    
    def __init__(self, string) -> None:
        self.__letter_count = utils.count_letters(string)
        self.__total_letters = utils.total_letters(string)
        self.__total_length = len(string)
        self.__letter_frequency = lf.letter_frequency(string)
        self.__index_of_coincidence = ioc.ioc(string)
        
    def get_letter_count(self):
        return self.__letter_count
        
    def get_total_letters(self):
        return self.__total_letters
        
    def get_total_length(self):
        return self.__total_length
        
    def get_letter_frequency(self):
        return self.__letter_frequency
        
    def get_(self):
        pass
        
    def get_(self):
        pass
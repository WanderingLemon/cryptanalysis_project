from frequency import letter_frequency as lf, utils

def test_total_letters():
    #setup
    string = utils.ENGLISH_ALPHABET
    expected = 26
    
    #invoke
    actual = utils.total_letters(string)
    
    #analyze
    assert actual == expected
    
def test_count_letters():
    #setup
    string = utils.ENGLISH_ALPHABET
    
    #invoke
    returned = utils.count_letters(string)
    
    #analyze
    for key in returned:
        value = returned[key]
        assert value == 1
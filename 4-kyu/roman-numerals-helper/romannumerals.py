'''
@test.describe('sample_tests')
def sample_tests():
    @test.it('to roman')
    def sample_tests_to():
        test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        test.assert_equals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        test.assert_equals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        test.assert_equals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
    @test.it('from roman')
    def sample_tests_from():
        test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        test.assert_equals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        test.assert_equals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        test.assert_equals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
'''

'''
class RomanNumerals:
    @staticmethod
    def to_roman(val):
        return ''

    @staticmethod
    def from_roman(roman_num):
        return 0
'''

# entra int para el val y str para el roman_num

# de valor a roman:

mil = None
cien = None
diez = None
uno  = None

val = 2345

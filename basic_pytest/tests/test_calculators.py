'''
The module test functionality of calculators.py
'''

import pytest
from basic_pytest.calculators import number_to_power, number_addition, number_substract

def test_calculator_with_int1():
    assert 9 == number_to_power(3,2)
    
def test_calculator_with_int2():
    assert 8 == number_to_power(2, 3)

def test_calculator_with_floats():
    ''' assert can test with approximation stated in params 
    
    example two decimal places 
    '''
    assert 9.53 == pytest.approx(number_to_power(3.5, 1.8), 0.2)
    
def test_calculator_expection():
    with pytest.raises(TypeError):
        number_to_power('a', 2)
    
    
class TestAddMinus():
    ''' group together tests for addition and substruction
    
    Show possibility of grouping together tests which are conected with some logic.
    For example following test single function
    '''
    
    def test_addtion_int(self):
        assert 5 == number_addition(2, 3)
    
    def test_addtion_float(self):
        assert 5.6 == number_addition(2.1, 3.5)

    def test_addtion_exception(self):
        with pytest.raises(TypeError):
            number_addition(2, 'a')
            
    def test_substract_int(self):
        assert -1 == number_substract(2, 3)
    
    def test_substract_float(self):
        assert -1.4 == number_substract(2.1, 3.5)

    def test_substract_exception(self):
        with pytest.raises(TypeError):
            number_addition(2, 'a')


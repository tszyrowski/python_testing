'''
Created on 19 Jul 2019

@author: T
'''

from basic_pytest.calculators import number_to_power
import pytest

def test_calculator_with_int1():
    assert 9 == number_to_power(3,2)
    
def test_calculator_with_int2():
    assert 8 == number_to_power(2, 3)

def test_calculator_with_floats():
    assert 9.53 == pytest.approx(number_to_power(3.5, 1.8), 0.2)
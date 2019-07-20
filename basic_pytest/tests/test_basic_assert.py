'''
test cover for basic asserts
'''
import pytest
from basic_pytest.basic_assert import simple_f

@pytest.mark.skip(reason="assert failure basic, comment out to see")
def test_function():
    assert simple_f() == 4
    
def test_message():
    """ show message on failure
    
    ====================================================== FAILURES =======================================================
____________________________________________________ test_message _____________________________________________________
    
        def test_message():
            ''' show message on failure
            '''
            a = 3
    >       assert a % 2 == 0, "Value was odd, should be even"
    E       AssertionError: Value was odd, should be even
    E       assert (3 % 2) == 0
    
    basic_pytest\basic_assert_test.py:19: AssertionError
    =================================== 1 failed, 11 passed, 2 skipped in 0.95 seconds ====================================
    """
    a = 3
    assert a % 2 == 0, "Value was odd, should be even"
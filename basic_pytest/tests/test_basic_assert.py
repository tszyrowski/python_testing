'''
test cover for basic asserts

Failing tests are marked as expected failure
To run them without changing the code:
& pytest --runxfail .\basic_pytest\tests\test_basic_assert.py

'''
import pytest

#===============================================================================
# Helper function
#===============================================================================

def simple_f():
    return 3

def simple_exception():
    ''' raising Exception for testing purpose'''
    raise ValueError("Exception 123 raised")

def simple_params(param1, param2=1):
    ''' take params to show testing functionality '''
    return param1 + param2

#===============================================================================
# Tests
#===============================================================================

@pytest.mark.xfail
def test_function():
    ''' Compare return valu with expected, 
    testing should fail, so it is annotated
    ''' 
    assert simple_f() == 4

@pytest.mark.xfail(raises=AssertionError)
def test_function_detail_xfail():
    ''' can be more specific why it fails
    if different exception raised, still fails
    '''
    assert simple_f() == 4

@pytest.mark.xfail
def test_message():
    """ show message on failure
    >>> (vPTesing) PS > pytest .\basic_pytest\tests\test_basic_assert.py
    
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
    
    >       assert simple_f() % 2 == 0, "Value was odd, should be even"
    E       AssertionError: Value was odd, should be even
    E       assert (3 % 2) == 0
    E        +  where 3 = simple_f()
    
    basic_pytest\tests\test_basic_assert.py:63: AssertionError
    ==================================== 1 failed, 5 passed, 3 xfailed in 0.49 seconds ====================================
    """
    assert simple_f() % 2 == 0, "Value was odd, should be even"
    
def test_zerodivision():
    ''' the test pass if exception is raised 
    '''
    with pytest.raises(ZeroDivisionError):
        1/0
        
def test_expection_with_check():
    ''' exception can be checked if has correct message
    '''
    with pytest.raises(Exception) as my_excinfo:        # create a wrapper around raised exception
        def f():    # will cause RuntimeError
            f()
        f()
    assert "maximum recursion" in str(my_excinfo.value) # wrapper has .type, .value, .traceback
    
def test_simple_exception():
    ''' exception message can be matched with re.search in context manager
    
    Note: the simple_exception() raises exception with ValueError("Exception 123 raised")
    '''
    with pytest.raises(ValueError, match=r".* 123 .*"):
        simple_exception()
        
def test_simple_param_oneliner():
    ''' exception can be checked in one line 
    
    Note: the simple_params takes to numeric values, when string given:
    TypeError: can only concatenate str (not "int") to str
    '''
    pytest.raises(TypeError, simple_params, "a", param2=2)
    
def test_simple_param_explicit():
    ''' exception can be with explicit call
    
    Note: Exceptions can be generalised, though it is not recomended
    '''
    with pytest.raises(Exception):
        simple_params("a", param2=2)
        

#===============================================================================
# SHOW DETAILED OUTPUT
#===============================================================================

@pytest.mark.xfail(raises=AssertionError)
def test_set_comparison():
    ''' the output explain in details what is different
    
    E       AssertionError: assert {'0', '1', '2', '3'} == {'1', '2', '3'}
    E         Extra items in the left set:
    E         '0'
    E         Full diff:
    E         - {'2', '1', '3', '0'}
    E         ?               -----
    E         + {'2', '1', '3'}
    '''
    set1 = set("1230")
    set2 = set("3211")
    assert set1 == set2
    

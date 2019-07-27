r'''
This script shows creation of a custom messages and comparisons
Pytest can performe custom comparison. The comparison and the custom message 
is created in coftest.py

The custom message will be automatically imported and used in the output such as:

>>> (vPTesing) PS > pytest .\basic_pytest\tests\test_foocompare.py

=========================== test session starts ================================
platform win32 -- Python 3.7.0, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: ..\python_testing
plugins: cov-2.7.1
collected 1 item

basic_pytest\tests\test_foocompare.py F                                   [100%]

============================ FAILURES ==========================================
_____________________ test_compare_custom_msg __________________________________

    def test_compare_custom_msg():
        f1 = Foo(1)
        f2 = Foo(2)
>       assert f1 == f2
E       assert comparison Foo instances
E          vals: 1 != 2

basic_pytest\tests\test_foocompare.py:36: AssertionError
================== 1 failed in 0.22 seconds ====================================
'''
import pytest

class Foo():
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val


@pytest.mark.xfail(raises=AssertionError)
def test_compare_custom_msg():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
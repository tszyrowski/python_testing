'''
the custom message is created in coftest.py

The custom message will be automatically imported and used in the output such as:

basic_pytest/tests/test_foocompare.py::test_compare_custom_msg FAILED    [100%]

================================== FAILURES ===================================
___________________________ test_compare_custom_msg ___________________________

    def test_compare_custom_msg():
        f1 = Foo(1)
        f2 = Foo(2)
>       assert f1 == f2
E       assert comparison Foo instances
E          vals: 1 != 2

basic_pytest\tests\test_foocompare.py:15: AssertionError
========================== 1 failed in 0.19 seconds ===========================
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
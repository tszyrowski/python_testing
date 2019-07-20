'''
module create custom comparison message
'''
from basic_pytest.tests.test_foocompare import Foo

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return["comparison Foo instances", " vals: %s != %s" %(left.val, right.val)]
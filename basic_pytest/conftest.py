'''
module create custom comparison message
'''
import pytest
from basic_pytest.tests.test_foocompare import Foo


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return["comparison Foo instances", " vals: %s != %s" %(left.val, right.val)]
        
@pytest.fixture
def myfuncarg(request):
    ''' in original example at:
    https://pytest.readthedocs.io/en/2.0.3/funcargs.html
    the name was different and fixture decorator was not provided
    but it was not discovered
    '''
    return 42

@pytest.fixture
def my_called_once(scope="module"):
    ''' as it is with module scope it is created when module is run
    by default it would be when test is executed
    Possible values for scope are: function, class, module, package or session.
    '''
    return 1
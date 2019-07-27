'''
Present the order in which fixtures are declered

The module uses fixtures created on conftest call appending to order=[]
'''

def test_fixture_auto_first_call(take_order):
    '''
    the order will have here only fixture with autouse=True
    '''
    assert take_order == ['a1']

    
def test_fixture_order(f1, m1, f2, s1, take_order):
    '''
    1. s1: is the highest-scoped fixture (session).
    2. m1: is the second highest-scoped fixture (module).
    3. a1: is a function-scoped autouse fixture: it will be instantiated before other fixtures within the same
    scope.
    4. f3: is a function-scoped fixture, required by f1: it needs to be instantiated at this point
    5. f1: is the first function-scoped fixture in test_foo parameter list.
    6. f2: is the last function-scoped fixture in test_foo parameter list
    
    BUT: 'a1' is already in the order so will be there first.
    If previous function would not be called, it would not be there 
    '''
    assert take_order == ['a1', 's1', 'm1','a1', 'f3', 'f1', 'f2']
    
def test_fixture_auto_last_call(take_order):
    '''
    in here we call order return and autouse=True is called again
    '''
    assert take_order == ['a1', 's1', 'm1','a1', 'f3', 'f1', 'f2', 'a1']
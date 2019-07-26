'''
Examples of different interesting tests
'''
import pytest
import os

# Creating temprary directory
def test_needs_files(tmpdir):       # create temproraty directory
    ''' this test will create temporary directory 
    
    tempdir is pytest fixture and it is a factory 
    '''
    assert os.path.isdir(tmpdir)
    
# skipping tests which will fail
@pytest.mark.skip(reason="no way of currently testing this")
def test_fail():
    assert 0
    
class MyPlugin():
    pass
    
''' pytest can be called with main and run as python module if needed
It can also accept command line arguments for example -x (stop after first failure
it would be called from command line:
pytest -x
'''
pytest.main(["-x"], plugins=[MyPlugin()])

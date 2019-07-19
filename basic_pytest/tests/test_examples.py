'''
Examples of different interesting tests
'''
import pytest
import os

# Creating temprary directory
def test_needs_files(tmpdir):       # create temproraty directory
    assert os.path.isdir(tmpdir)
    
# skipping tests which will fail
@pytest.mark.skip(reason="no way of currently testing this")
def test_fail():
    assert 0
    
pytest.main()

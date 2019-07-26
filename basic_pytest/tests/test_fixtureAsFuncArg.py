'''
test function can receive fixture object as named input arg
'''
import pytest


@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    # the msg is of the format:
    # b'smtp.gmail.com at your service, [195.188.41.116]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8'
    assert b'smtp.gmail.com at your service' in msg
    assert b'\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8' in msg
    
@pytest.mark.xfail
def test_1(myNonExistingFixture):
    ''' available fixtures: cache, 
                            capfd, 
                            capfdbinary, 
                            caplog, 
                            capsys, 
                            capsysbinary, 
                            cov, 
                            doctest_namespace, 
                            monkeypatch, 
                            no_cover, 
                            pytestconfig, 
                            record_property, 
                            record_testsuite_property, 
                            record_xml_attribute, 
                            recwarn, 
                            smtp_connection, 
                            tmp_path, 
                            tmp_path_factory, 
                            tmpdir, 
                            tmpdir_factory
    '''

    assert 1
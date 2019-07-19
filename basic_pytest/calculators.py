'''
Module contains basic functions
'''

def number_to_power(number, power):
    '''
    :param number: number to be taken 
    :param power: 
    :return: number to power
    
    >>> number_to_power(3, 2)
    9
    >>> number_to_power(2, 3)
    8
    '''
    return number**power

if __name__=='__main__':
    print(number_to_power(3.5,2.1))
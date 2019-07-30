'''
The class for presenting bdd-test

'''

class NinjaFight(object):
    '''
    Domain model for ninja
    '''
    
    def __init__(self, with_ninja_level=None):
        self.with_ninja_level = with_ninja_level
        self.oponent = None
        
    def decision(self):
        '''
        Business logic how Ninja should react 
        '''
        assert self.with_ninja_level in not None
        assert self.oponent is not None
        if self.oponent == "Chuck Norris":
            return "run for his life"
        if "black-belt" in self.with_ninja_level:
            return "engage the oponent"
        else:
            return "run for his life"
        
        
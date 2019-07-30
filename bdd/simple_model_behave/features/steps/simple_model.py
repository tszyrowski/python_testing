'''
this test is in response to simple_model feature

Tests response of the ninja in relation to strength of the oponent
'''

import behave

@behave.given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    context.ninja_figt = NinjaFigt(achievement_level)
    
@behave.when('attacked by a {opponent_role}')
def step_attacke_by_a(context, oponent_role):
    context.ninja_fight.oponent = oponent_role
    
@behave.when('attacked by a {opponent}')
def step_attacked_by(context, oponent):
    context.ninja_fight.oponent = oponent
    
@behave.then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    assert reaction == context.ninja_fight.deciosion()
'''
test for basic behave BDD

/python_testing/basic_bdd_behave (bdd-basic)
$ behave
Feature: Showing off behave # features/tutorial.feature:20

  Scenario: run a simple test       # features/tutorial.feature:22
    Given we have behave installed  # features/steps/tutorial.py:6
    When we implement a test        # features/steps/tutorial.py:10
    Then behave will test it for us # features/steps/tutorial.py:14

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.002s
'''
import behave

@behave.given('we have behave installed')
def step_impl(context):
    pass

@behave.when('we implement a test')
def step_impl(context):
    assert True is not False
    
@behave.then('behave will test it for us')
def step_impl(context):
    assert context.failed is False


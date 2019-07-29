'''
Created on 29 Jul 2019

@author: T
'''
@given('a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel()
    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])
        
@when()
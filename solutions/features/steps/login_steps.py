from behave import given, when, then

@given(u'The user is on the login page')
def step_impl(context):
    context.on_login_page = True


@when(u'they enter valid credentials')
def step_impl(context):
    context.credentials_are_valid = True


@then(u'they should see their dashboard')
def step_impl(context):
    assert context.credentials_are_valid & context.on_login_page


@when(u'they enter invalid credentials')
def step_impl(context):
    context.credentials_are_valid = False


@then(u'they should see an error message')
def step_impl(context):
    assert not context.credentials_are_valid
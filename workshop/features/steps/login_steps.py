from behave import given, then, when


@given("The user is on the login page")
def step_impl(context):
    context.on_login_page = True


@when("they enter valid credentials")
def step_impl(context):
    context.credentials_are_valid = True


@then("they should see their dashboard")
def step_impl(context):
    assert context.credentials_are_valid & context.on_login_page

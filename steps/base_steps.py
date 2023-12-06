from behave import *

@then('base: I can see my account in the menu')
def step_impl(context):
    context.base_page.verify_my_account_is_displayed()
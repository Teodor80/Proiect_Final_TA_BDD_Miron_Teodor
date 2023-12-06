from behave import *


@when('forgot_pass: I fill in my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)

@when('forgot_pass: I click on the recover button')
def step_impl(context):
    context.forgot_password_page.click_recover_button()

@when('forgot_pass: I make sure the email input is cleared')
def step_impl(context):
    context.forgot_password_page.clear_email()

@then('forgot_pass: I verify the invalid email validation message "{msg}"')
def step_impl(context, msg):
    context.forgot_password_page.verify_email_error_message(msg)

@then('forgot_pass: I verify the notification "{notif}"')
def step_impl(context, notif):
    context.forgot_password_page.verify_notification_message(notif)

@when('forgot_pass: I proceed if email field is not empty')
def proceed_if_email_not_empty(context):
    email = context.scenario_outline['email']
    if not email:
        raise Exception("Email field is empty. Test will be marked as failed.")

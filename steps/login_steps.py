from behave import *

@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('login: I click on the forgot password link')
def step_impl(context):
    context.login_page.click_forgot_password_link()

@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I fill in a password "{psw}"')
def step_impl(context, psw):
    context.login_page.set_password(psw)

@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('login: I verify the email is wrong validation message "{notif}"')
def step_impl(context, notif):
    context.login_page.verify_notification_message(notif)
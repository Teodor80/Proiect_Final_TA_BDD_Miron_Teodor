from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "user_login")
    PASSWORD_INPUT = (By.ID, "user_password")
    LOGIN_BUTTON = (By.ID, "submit_button")
    FORGOT_PASSWORD_LINK = (By.XPATH, '//span[contains(@class, "forgot-password-btn") and text()="Forgot password?"]')
    INNCORECT_EMAIL = (By.ID, "flash_alert")


    def navigate_to_login_page(self):
        self.driver.get("https://www.strikingly.com/s/login?locale=en")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, pswrd):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(pswrd)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def verify_notification_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.INNCORECT_EMAIL).text
        except NoSuchElementException:
            actual_message = 'None'

        assert actual_message == expected_message, f'Error, the message is incorrect, expected {expected_message}, actual {actual_message}'

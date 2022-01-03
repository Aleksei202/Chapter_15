import time

from behave import given, when, then

from BrainBucket.webelements.browser import Browser
from BrainBucket.pages.forgotten_password_page import ForgottenPasswordPage
from BrainBucket.pages.login_page import LoginPage
from BrainBucket.utils.config_reader import ConfigReader

URL = "https://techskillacademy.net/brainbucket/index.php?route=account/forgotten"
configs = ConfigReader("config.ini")


@given("forgotten password page is launched")
def launch_forgotten_password_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser


@when("user enters account email")
def enter_email(context):
    forgotten_password_page = ForgottenPasswordPage(context.browser)
    forgotten_password_page.enter_email(configs.get_email('user1'))
    time.sleep(3)
    context.forgotten_password_page = forgotten_password_page


@when("user clicks 'continue' button")
def click_login_button(context):
    forgotten_password_page = context.forgotten_password_page
    forgotten_password_page.click_continue_btn()
    time.sleep(3)


@then("info pops up about success email")
def verify_email_sent_text(context):
    login_page = LoginPage(context.browser)
    context.login_page = login_page
    login_page.verify_email_sent_text()


@then("user gets info that email is not registered")
def verify_email_fail(context):
    forgotten_password_page = context.forgotten_password_page
    forgotten_password_page.verify_email_not_exist_text()

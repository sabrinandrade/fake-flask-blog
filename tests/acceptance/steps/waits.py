from behave import *
from selenium.webdriver.support.wait import *
from selenium.webdriver.support import expected_conditions
from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


@given('I wait for the posts to load')
def self_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BlogPageLocators.POST_SECTION)
    )

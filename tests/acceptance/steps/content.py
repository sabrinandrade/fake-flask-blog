from behave import *
from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@then("There is a title shown on the page")
def step_impl(context):
    # Given the app is so small, we can search for the h1 tag
    # and have confidence that it will be the title
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


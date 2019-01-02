from behave import *

use_step_matcher('re')


@when('I click the button with id "(.*)"')
def step_impl(context, link_id):
    element = context.driver.find_element_by_id(link_id)
    element.click()


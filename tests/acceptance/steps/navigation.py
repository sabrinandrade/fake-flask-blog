from behave import *
from selenium import webdriver
from tests.driver_configuration import chrome_path

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome(chrome_path)
    browser.get("http://127.0.0.1:5000")



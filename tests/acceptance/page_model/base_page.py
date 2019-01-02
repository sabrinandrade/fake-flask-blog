from tests.acceptance.locators.base_page import BasePageLocators

'''
Why go through so much hassle with the locators and the models?
Because it makes it simpler to maintain the system

This class contains everything generic and identical to different parts of the system
'''


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Since the methods don't take any arguments, you can use the @property decorator
    # Every time you call this method, just treat it as an attribute instead of a method
    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        # The * deconstructs the tuple created in the base page locator and passes it as two different values
        # because find_element takes two arguments
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

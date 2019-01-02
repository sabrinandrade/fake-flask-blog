from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.blog_page import BlogPageLocators


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POST_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.NEW_POST_LINK)

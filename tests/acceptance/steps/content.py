from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

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


@then('I can see there is a post section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, post_title):
    page = BlogPage(context.driver)
    posts_matching_title = [p for p in page.posts if p.text == post_title]

    assert len(posts_matching_title) > 0
    assert all([post.is_displayed() for post in posts_matching_title])


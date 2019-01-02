from selenium.webdriver.common.by import By


class NewPostLocators:
    NEW_POST_FORM = By.ID, 'post-form'
    TITLE_FIELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'
    NAV_LINKS = By.CLASS_NAME, 'nav-link'

Feature: Test navigation between pages

  Scenario: Homepage can go to the Blog page
    Given I am on the homepage
    When I click the button with id "blog-link"
    Then I am on the blog page

  Scenario: Blog page can go to Homepage
    Given I am on the blog page
    When I click the button with id "home-link"
    Then I am on the homepage

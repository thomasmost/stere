import logging
import os

from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)


def test_is_visible(test_page):
    test_page.navigate()
    assert test_page.added_container.is_visible(wait_time=6)


def test_is_not_visible(test_page):
    test_page.navigate()
    assert test_page.removed_container.is_not_visible(wait_time=6)


def test_is_present_args(test_page):
    """
    When I send an argument to is_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.added_container.is_present(wait_time=6)


def test_is_not_present_args(test_page):
    """
    When I send an argument to is_not_present
    Then it is used by the correct function
    """
    test_page.navigate()
    assert test_page.removed_container.is_not_present(wait_time=6)


def test_button_data_star_strategy(browser, test_page):
    """
    When I define a Field using a data-* strategy, it is found.
    """
    test_page.navigate()
    test_page.button_alt_strategy.click()

    # Clicking changes the button's container background colour
    browsers = {
     'firefox': 'rgb(255, 0, 0)',
     'chrome': 'rgba(255, 0, 0, 1)',
    }

    # This works because value_of_css_property is gotten from splinter,
    # which gets it from Selenium
    actual = test_page.button_container.first._element.value_of_css_property(
        'background-color')
    assert browsers[os.environ["CURRENT_BROWSER_NAME"]] == actual


def test_data_star_staregy_is_present(browser, test_page):
    test_page.navigate()
    assert test_page.button_alt_strategy.is_present(wait_time=3)


def test_data_star_staregy_is_not_present(browser, test_page):
    test_page.navigate()
    assert test_page.missing_button.is_not_present(wait_time=3)
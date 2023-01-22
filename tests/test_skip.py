"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот) с помощью марки скип
"""
import pytest
from selene.support.shared import browser
from model.pages.github_page import open_page,\
    click_button_sign_in,\
    click_button_hamburger,\
    check_header_sign_in


@pytest.fixture()
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_github_desktop(browser_config):
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        pytest.skip("Размер окна под мобильную версию!")
    else:
        open_page()
        click_button_sign_in()
        check_header_sign_in()


def test_github_mobile(browser_config):
    if browser.config.window_width == 900 and browser.config.window_height == 940:
        pytest.skip("Размер окна под десктопную версию!")
    else:
        open_page()
        click_button_hamburger()
        click_button_sign_in()
        check_header_sign_in()
"""1. Чистый Selene (без шагов)"""
from selene import browser, have, be, by


def test_check_issue_name_only_selene():
    browser.open('http://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.all('[aria-label=Issues][role=group]').element_by(have.text('#81')).should(be.visible)

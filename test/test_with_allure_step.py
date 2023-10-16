"""2. Лямбда шаги через with allure.step"""
from selene import have, be, by
from selene.support.shared import browser
import allure


def test_check_issue_name_with_allure_step():
    allure.dynamic.title('Проверка наличия наличия Issue в репозитории')
    allure.dynamic.tag('Github web')
    allure.dynamic.severity(severity_level='Critical')
    allure.dynamic.feature('Issues tab')
    allure.dynamic.story('Использование with allure.step')
    allure.dynamic.link("https://github.com/", name='test_issues_name')
    allure.dynamic.label('owner', '#81 issue_to_test_allure_report')

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Выполняем поиск нужного репозитория'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Выполняем вход в найденный репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Выполняем поиск нужного Issues'):
        browser.all('[aria-label=Issues][role=group]').element_by(have.text('#81')).should(be.visible)

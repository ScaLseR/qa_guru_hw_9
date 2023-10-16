"""3. Шаги с декоратором @allure.step"""
import allure
from selene import have, be, by
from selene.support.shared import browser
from allure_commons.types import Severity

URL = 'https://github.com/'


@allure.title('Проверка наличия наличия Issue в репозитории')
@allure.tag('Github web')
@allure.severity(severity_level='Critical')
@allure.label('owner', '#81 issue_to_test_allure_report')
@allure.feature('Issues tab')
@allure.story('Использование декораторов @allure.step')
@allure.link('https://github.com/', 'test_issues_name')
def test_check_issue_name_with_allure_decorator():
    open_main_page()
    find_repo()
    enter_repo()
    open_issue_tab()
    find_issue()


@allure.step(f'Открываем главную страницу {URL}')
def open_main_page():
    browser.open(URL)


@allure.step('Выполняем поиск нужного репозитория')
def find_repo():
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()


@allure.step('Выполняем вход в репозиторий')
def enter_repo():
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step('Открываем вкладку Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Выполняем поиск нужного Issues')
def find_issue():
    browser.all('[aria-label=Issues][role=group]').element_by(have.text('#81')).should(be.visible)

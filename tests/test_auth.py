
import pytest

from settings import PASSWORD, PHONE
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage


@pytest.mark.parametrize("url", ["https://lk.rt.ru/", "https://my.rt.ru/",
                                 "https://start.rt.ru/",
                                 "https://lk.smarthome.rt.ru/",
                                 "https://key.rt.ru/"])
def test_authorisation_check_elements_in_forms(web_browser, url):
    """Checks for the presence of elements on the web page in all rostelecom products:
    https://lk.rt.ru/, https://my.rt.ru/, https://start.rt.ru/, https://lk.smarthome.rt.ru/, https://key.rt.ru/"""

    page = AuthPage(web_browser, url)
    page.wait_page_loaded()
    if url == ("https://lk.rt.ru/" or "https://start.rt.ru/"):
        if url == "https://start.rt.ru/":
            page.button_enter_with_password.click()
            page.wait_page_loaded()
        assert page.user_name.is_presented()
        assert page.password.is_presented()
        assert page.tab_phone.is_presented()
        assert page.tab_email.is_presented()
        assert page.tab_login.is_presented()
        assert page.tab_l_s.is_presented()
        assert page.button_enter.is_presented()
    else:
        if url == "https://key.rt.ru/":
            page.button_enter_for_key_rt.click()
            page.wait_page_loaded()

        if page.button_enter_with_password.is_presented():
            page.button_enter_with_password.click()
            page.wait_page_loaded()

            assert page.user_name.is_presented()
            assert page.password.is_presented()
            assert page.tab_phone.is_presented()
            assert page.tab_email.is_presented()
            assert page.tab_login.is_presented()
            assert page.button_enter.is_presented()
    web_browser.quit()


def test_auth_page_check_change_tab(web_browser):
    """checks auto-change tabs phone, mail, login, personal account on the web page"""

    page = AuthPage(web_browser, url="https://lk.rt.ru/")
    page.wait_page_loaded()
    page.message_for_test_in_page("Идет проверка автоматической идентификации нужного таба")
    # проверим - стартовый таб
    assert 'active' in page.tab_phone.get_attribute('class')

    page.user_name.send_keys('mail@mail.ru')
    page.user_name.send_keys(Keys.TAB)
    # проверим - меняется ли таб почта
    assert 'active' in page.tab_email.get_attribute('class')

    page.user_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    page.user_name.send_keys('123456789101')
    page.user_name.send_keys(Keys.TAB)
    # проверим - меняется ли таб лицевой счет
    assert 'active' in page.tab_l_s.get_attribute('class')

    page.user_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    page.user_name.send_keys('varvara675')
    page.user_name.send_keys(Keys.TAB)
    # проверим - меняется ли таб логин
    assert 'active' in page.tab_login.get_attribute('class')

    page.tab_email.click()
    page.user_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    page.user_name.send_keys('+79000000000')
    page.user_name.send_keys(Keys.TAB)
    # проверим - меняется ли таб телефон
    assert 'active' in page.tab_phone.get_attribute('class')
    web_browser.quit()


def test_auth_page_phone_check_valid_format(web_browser):
    """Checks the phone input format - positive"""

    page = AuthPage(web_browser, url="https://lk.rt.ru/")
    page.wait_page_loaded()

    # проверим валидацию формата номера телефона
    page.message_for_test_in_page("Идет проверка валидации правильного формата телефона")
    page.user_name.send_keys("+79000000000")
    page.user_name.send_keys(Keys.TAB)

    assert not page.span_incorrect_phone_format.is_visible()
    web_browser.quit()


def test_auth_page_phone_check_not_valid_format(web_browser):
    """Checks the phone input format - negative"""

    page = AuthPage(web_browser, url="https://lk.rt.ru/")
    page.wait_page_loaded()

    # проверим валидацию формата номера телефона
    page.message_for_test_in_page("Идет проверка валидации правильного формата телефона")
    page.user_name.send_keys("+7900000000")
    page.user_name.send_keys(Keys.TAB)

    assert page.span_incorrect_phone_format.is_visible()
    web_browser.quit()


def test_authorisation_for_phone_negative(web_browser):
    """verification of authorization with invalid parameters - orange color of the forgot password button"""

    page = AuthPage(web_browser, url="https://lk.rt.ru/")
    page.wait_page_loaded()
    page.message_for_test_in_page("Проверка перекрашивания кнопки Забыл пароль в оранжевый цвет")
    page.wait_page_loaded(sleep_time=1.5)
    page.user_name.send_keys("+79000000000")
    page.password.send_keys("not_valid_password")
    page.button_enter.click()

    # проверим перекрашиваться ли "Забыл пароль" в оранжевый цвет
    assert 'animated' in page.button_forgot_password.get_attribute('class')
    # проверим выводиться ли сообщение "Неверный логин или пароль"
    assert page.span_invalid_username_or_password.is_visible()
    web_browser.quit()


def test_authorisation_for_phone_positive(web_browser):
    """let's check the authorization in the system according to a positive scenario"""
    page = AuthPage(web_browser, url="https://lk.rt.ru/")
    page.wait_page_loaded()

    # проверим авторизацию в системе по позитивному сценарию
    page.message_for_test_in_page("Вход в систему с валидными данными")
    page.user_name.send_keys(PHONE)
    page.password.send_keys(PASSWORD)
    page.button_enter.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    web_browser.quit()

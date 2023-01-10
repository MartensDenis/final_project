import os
import pickle

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPageTemp(WebPage):

    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    # локаторы для auth_temp_page
    input_address = WebElement(id='address')
    button_get_code = WebElement(id="otp_get_code")
    input_code = WebElement(id="rt-code-0")
    button_go_lk = WebElement(xpath='//a[contains(text(), "Перейти")]')
    countdown = WebElement(css_selector='.otp-form__timeout')
    # сообщения системы
    hint_enter_the_number = WebElement(xpath="//p[contains(text(),'Укажите почту или номер телефона')]")

    #если вдруг каптча
    captcha = WebElement(css_selector=".rt-captcha__image")
    captcha_input = WebElement(id='captcha')

    # личный кабинет
    button_lk = WebElement(id="lk-btn")

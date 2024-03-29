import time

import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 6)

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.driver.find_element(*MainPage.button_coockie).click()

    def wait_load_main_page(self):
        self.wait.until(EC.visibility_of_element_located(MainPage.home_page))

    @allure.step('Нажимаем кнопку "Заказать" в хидере страницы')
    def click_button_order_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_middle))
        self.driver.find_element(*MainPage.button_order_header).click()

    @allure.step('Скролим страницу до кнопки "Заказать"')
    def scroll_button_order_middle(self):
        el = self.driver.find_element(*MainPage.sroll_button_midle)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.wait.until(EC.visibility_of_element_located(MainPage.sroll_button_midle))
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_middle))

    @allure.step('Нажимаем кнопку "Заказать" в середине страницы')
    def click_button_order_middle(self):
        self.driver.find_element(*MainPage.button_order_middle).click()

    @allure.step('Нажимаем кнопку лого Самоката')
    def click_logo_scooter(self):
        self.driver.find_element(*MainPage.logo_scooter).click()
        self.wait.until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/'))

    @allure.step('Нажимаем кнопку лого Яндекса')
    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.logo_yandex))
        self.driver.find_element(*MainPage.logo_yandex).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)




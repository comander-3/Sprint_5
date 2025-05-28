from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
import helpers
import data
from urls import Urls

class TestPostAnnonce:
    def test_post_unauthorized_user(self, driver, open_browser):
        open_browser
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_post_annonce))
        driver.find_element(*Locators.button_post_annonce).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.window_unauthorized))
        assert driver.find_element(*Locators.window_unauthorized)

    def test_post_authorized_user(self, driver, open_browser):
        open_browser
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_enter_register))
        driver.find_element(*Locators.button_enter_register).click() # вход и регистрация
        helpers.log_in(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar))
        driver.find_element(*Locators.button_post_annonce).click()
        driver.find_element(*Locators.input_name).send_keys(data.ANNONCE['name'])  # заполнение поля "Название"
        driver.find_element(*Locators.input_description).send_keys(data.ANNONCE['about'])  # заполнение поля "Описание"
        driver.find_element(*Locators.input_price).send_keys(data.ANNONCE['price'])  # заполнение поля "Название"
        driver.find_element(*Locators.button_dropdown_category).click()  # раскрытие списка категории
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.span_auto))
        driver.find_element(*Locators.div_radio_used).click()  # выбор состояния "Б/У"
        driver.find_element(*Locators.button_dropdown_city).click()  # раскрытие списка городов
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.span_city))
        driver.find_element(*Locators.span_auto).click()  # выбор категории "Авто"  #//
        driver.find_element(*Locators.span_city).click()  # выбор города "Новосибирск"
        driver.find_element(*Locators.button_post_publish).click() # публикация объявления
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.input_search))
        driver.find_element(*Locators.button_profile).click()  # открытие страницы профиля
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.title_my_annonce))
        element = driver.find_element(*Locators.title_my_annonce)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        annonce_title = driver.find_element(*Locators.annonce_name).text
        assert annonce_title == data.ANNONCE['name']

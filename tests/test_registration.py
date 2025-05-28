from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
import helpers
import data
from urls import Urls

class TestRegistration:
    def test_registration_success(self, driver, open_browser):
        open_browser
        driver.find_element(*Locators.button_enter_register).click() # вход и регистрация
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click()  # нажатие кнопки "Нет аккаунта"
        email = helpers.generate_email()
        password = helpers.generate_password()
        driver.find_element(*Locators.register_email).send_keys(email)
        driver.find_element(*Locators.register_password).send_keys(password)
        driver.find_element(*Locators.register_submit_password).send_keys(password)
        driver.find_element(*Locators.button_create_account).click()  # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar))
        assert (driver.current_url == Urls.url_registration) and (driver.find_element(*Locators.logo_avatar)) and (driver.find_element(*Locators.profile_name).text == 'User.')

    def test_registration_email_is_incorrect(self, driver, open_browser):
        open_browser
        driver.find_element(*Locators.button_enter_register).click() # вход и регистрация
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click()  # нажатие кнопки "Нет аккаунта"
        driver.find_element(*Locators.register_email).send_keys('com-3@test.')
        driver.find_element(*Locators.button_create_account).click()  # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.span_error_email))
        assert driver.find_element(*Locators.span_error_email)

    def test_registration_email_is_exists(self, driver, open_browser):
        open_browser
        driver.find_element(*Locators.button_enter_register).click() # вход и регистрация
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.button_no_account))
        driver.find_element(*Locators.button_no_account).click()  # нажатие кнопки "Нет аккаунта"
        driver.find_element(*Locators.register_email).send_keys(data.ACCOUNT['email'])
        driver.find_element(*Locators.register_password).send_keys(data.ACCOUNT['password'])
        driver.find_element(*Locators.register_submit_password).send_keys(data.ACCOUNT['password'])
        driver.find_element(*Locators.button_create_account).click()  # нажатие кнопки "Создать аккаунт"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.span_error_email))
        assert driver.find_element(*Locators.span_error_email)
   
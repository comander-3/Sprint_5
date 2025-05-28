from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
import helpers
from urls import Urls

class TestLogOut:
    def test_log_out_of_account(self, driver, open_browser):
        open_browser
        driver.find_element(*Locators.button_enter_register).click() # вход и регистрация
        helpers.log_in(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_exit))
        driver.find_element(*Locators.button_exit).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_enter_register))
        assert driver.find_element(*Locators.button_enter_register)

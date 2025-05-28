from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
import helpers
from urls import Urls

class TestLogIn:
    def test_log_in_to_account_button(self, driver, open_browser):
        open_browser      
        driver.find_element(*Locators.button_enter_register).click() # нажатие кнопки "вход и регистрация"
        helpers.log_in(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.logo_avatar))
        assert (driver.find_element(*Locators.profile_name).text == 'User.') and (driver.current_url == Urls.url_login) and (driver.find_element(*Locators.logo_avatar))

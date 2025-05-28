import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import Locators
from urls import Urls

@pytest.fixture()
def driver():   # фикстура создания драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_browser(driver):  # фикстура открытия главной страницы
    driver.get(Urls.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.logo_doska))

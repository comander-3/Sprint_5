import random
import string
import data
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def log_in(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_enter))
    driver.find_element(*Locators.login).send_keys(data.ACCOUNT['email'])
    driver.find_element(*Locators.password).send_keys(data.ACCOUNT['password'])
    driver.find_element(*Locators.button_enter).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_post_annonce))

def generate_email(domain='test.ru'):
    user_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.choice(range(3, 11))))
    return f"{user_name}@{domain}"

def generate_password():
    gen_password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(gen_password, k=random.choice(range(6, 10))))

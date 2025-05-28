from selenium.webdriver.common.by import By

class Locators:
    annonce_name = (By.XPATH, ".//div[@class='about']//h2[text()='Гараж каменный']")  # заголовок объявления в "Мои объявления"

    button_enter_register = (By.XPATH, ".//button[text() = 'Вход и регистрация']")  # кнопка "Вход и регистрация"
    button_no_account = (By.XPATH, ".//button[text() = 'Нет аккаунта']")  # кнопка "Нет аккаунта"
    button_create_account = (By.XPATH, ".//button[text() = 'Создать аккаунт']")  # кнопка "Создать аккаунт"
    button_enter = (By.XPATH, './/button[text() = "Войти"]')  # кнопка "Войти"
    button_exit = (By.XPATH, ".//button[text() = 'Выйти']")  # кнопка "Выйти" 
    button_post_annonce = (By.XPATH, './/button[text() = "Разместить объявление"]')  # кнопка "Разместить объявление"
    button_post_publish = (By.XPATH, './/button[text() = "Опубликовать"]')  # кнопка публикации объявления
    button_dropdown_category = (By.XPATH, ".//button[@class = 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")   # выпадающий список выбора категории нового объявления dropDownMenu_arrowUp__I25Xq dropDownMenu_noDefault__wSKsP
    button_dropdown_city = (By.XPATH, ".//button[@class = 'dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")   # выпадающий список выбора города  dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP
    button_profile = (By.XPATH, ".//button[@class = 'circleSmall']")   # кнопка профиля
    border_register_email = (By.XPATH, ".//div[@class='input_inputError__fLUP9']")  # рамка поля email в окне регистрации

    div_radio_used = (By.XPATH, ".//div[@class='radioUnput_inputActive__eC-HY']")  # переключатель состояния товара "Б/У" на странице размещения объявления

    input_name = (By.XPATH, ".//input[@name='name']")  # поле "Название" на странице размещения объявления
    input_description = (By.XPATH, ".//textarea[@name='description']")  # поле "Описание" на странице размещения объявления
    input_price = (By.XPATH, ".//input[@name='price']")  # поле "Стоимость" на странице размещения объявления
    input_search =  (By.XPATH, ".//input[@placeholder='Я хочу купить...']") # placeholder="Я хочу купить..."
    
    login = (By.NAME, "email")  # поле "Email" на странице входа
    logo_avatar = (By.XPATH, ".//*[name()='svg' and @class='svgSmall']")
    logo_doska = (By.XPATH, ".//*[name()='svg' and @class='header_logo__yAp5Y']")  # логотип "DOSKA"

    password = (By.NAME, "password")  # поле "Пароль" на странице входа
    page_new_annonce = (By.XPATH,".//h1[text()='Новое объявление']")  # страница создания нового бъявления "Новое объявление"
    profile_name = (By.XPATH, ".//h3[text()='User.']")

    register_email = (By.NAME, "email")  # поле "email" на странице регистрации
    register_password = (By.NAME, "password")  # поле "password" на странице регистрации
    register_submit_password = (By.NAME, "submitPassword")  # поле "submitPassword" на странице регистрации

    span_auto = (By.XPATH, "//span[text()='Авто']")  # категория нового объявления "Авто"
    span_city = (By.XPATH, "//span[text()='Новосибирск']")  # город размещения объявления "Новосибирск"
    span_error_email = (By.XPATH, "//span[text()='Ошибка']")  # ошибка регистрации email

    title_my_annonce = (By.XPATH, ".//h1[text()='Мои объявления']")

    window_unauthorized = (By.XPATH,".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")  # модальное окно сообщения неавторизованному пользователю

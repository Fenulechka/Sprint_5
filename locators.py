from selenium.webdriver.common.by import By


class TestLocators:
    # Локаторы для входа
    # вход по кнопке «Войти в аккаунт» на главной
    LOGIN_BUTTON_HOMEPAGE = [By.XPATH, ".//button[text()='Войти в аккаунт']"]

    # вход через кнопку «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"]

    # вход через кнопку в форме регистрации
    REGISTER_LOGIN_LINK = [By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]"]  # ссылка: Вы — новый пользователь? Зарегистрироваться
    LOGIN_LINK = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']"]  # ссылка: Уже зарегистрированы? Войти

    # вход через кнопку в форме восстановления пароля
    RESET_PASSWORD_LINK = [By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"]
    LOGIN_LINK = [By.XPATH,"//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']"]

    # Локаторы для регистрации аккаунта
    NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    PASSWORD = (By.XPATH, './/input[@name="Пароль"]')
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # сообщение об ошибке: Некорректный пароль
    INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    # Локаторы для входа в аккаунт
    EMAIL_LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_LOGIN = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    # Локаторы в личном кабинете
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@type = "button"]')

    # Локаторы для переходов по разделам
    # логотип в шапке профиля
    LOGO_SWITCHING = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

    # кнопка Конструктор в шапке профиля
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")

    # раздел Булки в конструкторе
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, '') and .//span[text()='Булки']]")

    # раздел Соусы в конструкторе
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and contains(., 'Соусы')]")

    # раздел Начинки в конструкторе
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') and contains(., 'Начинки')]")
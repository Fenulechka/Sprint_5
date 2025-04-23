from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для входа

    # вход по кнопке «Войти в аккаунт» на главной
    LOGIN_BUTTON_HOMEPAGE = [By.XPATH, "//button[text()='Войти в аккаунт']"]

    # вход через кнопку «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"]

    # вход через кнопку в форме регистрации
    REGISTER_LOGIN_LINK = [By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]"] # ссылка: Вы — новый пользователь? Зарегистрироваться
    LOGIN_LINK = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']"]

    # вход через кнопку в форме восстановления пароля
    RESET_PASSWORD_LINK = [By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"]
    LOGIN_LINK = [By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']"]

    # Локаторы для регистрации

    EMAIL = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Email']")
    PASSWORD = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти' and contains(@class, 'button_button__33qZ0')]")

    # Локаторы для переходов по разделам
    LOGO_SWITCHING = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    SECTION_ROLLS = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Булки']")
    SECTION_SAUCES = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']")
    SECTION_TOPPINGS = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']")

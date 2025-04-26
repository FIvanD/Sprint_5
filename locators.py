from selenium.webdriver.common.by import By


class Locators:

    REG_BUTTON = By.LINK_TEXT, "Зарегистрироваться"
    NAME_FIELD = By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[1]"
    EMAIL_FIELD = By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[2]"
    PASSWORD_FIELD = By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[3]"
    CONTINUE_REG_BUTTON = By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"


    LOGIN_MAIN_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text() = 'Личный Кабинет']"
    LOGIN = By.XPATH, "//button[text()='Войти']"
    LOGIN_BUTTON = By.LINK_TEXT, "Войти"
    REMEMBER_PASSWORD_BUTTON = By.LINK_TEXT, "Восстановить пароль"
    EMAIL_INPUT = By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[1]"
    PASSWORD_INPUT = By.XPATH, "(//input[@class = 'text input__textfield text_type_main-default'])[2]"

    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    LOGO_BUTTON = By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']/a"
    LOGOUT_BUTTON = By.XPATH, ".//button[text()= 'Выход']"

    BUNS = By.XPATH, "//span[contains(text(),'Булки')]"
    SAUCES = By.XPATH, "//span[contains(text(),'Соусы')]"
    FILLINGS = By.XPATH, "//span[contains(text(),'Начинки')]"
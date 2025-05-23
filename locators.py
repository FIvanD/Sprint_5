from selenium.webdriver.common.by import By


class Locators:

    REG_BUTTON = By.LINK_TEXT, "Зарегистрироваться"
    NAME_FIELD = By.XPATH, "//div[label[contains(text(),'Имя')]]//input"
    EMAIL_FIELD = By.XPATH, "//div[label[contains(text(),'Email')]]//input"
    PASSWORD_FIELD = By.XPATH, "//div[label[contains(text(),'Пароль')]]//input"
    CONTINUE_REG_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"


    LOGIN_MAIN_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text() = 'Личный Кабинет']"
    LOGIN = By.XPATH, "//button[text()='Войти']"
    LOGIN_BUTTON = By.LINK_TEXT, "Войти"
    REMEMBER_PASSWORD_BUTTON = By.LINK_TEXT, "Восстановить пароль"

    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    LOGO_BUTTON = By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']/a"
    LOGOUT_BUTTON = By.XPATH, ".//button[text()= 'Выход']"

    BUNS = By.XPATH, "//span[contains(text(),'Булки')]"
    SAUCES = By.XPATH, "//span[contains(text(),'Соусы')]"
    FILLINGS = By.XPATH, "//span[contains(text(),'Начинки')]"

    INVALID_PASSWORD_MESSAGE = By.XPATH, "//p[text() = 'Некорректный пароль']"
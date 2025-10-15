from selenium.webdriver.common.by import By


class MainPage:
    NAME_FIELD = ('id', 'name-input')
    PASSWORD_FIELD = ('xpath', '//input[@type="password"]')
    EMAIL_FIELD = ('id', 'email')
    MESSAGE_FIELD = ('id', 'message')

    FAV_DRINK_MILK = ('xpath', '//input[@name="fav_drink" and @value="Milk"]')
    FAV_DRINK_COFFEE = ('xpath', '//input[@name="fav_drink" and @value="Coffee"]')

    FAV_COLOR = ('xpath', '//input[@name="fav_color" and @value="Yellow"]') 

    QU_AUTOMATION = (By.CSS_SELECTOR, '#automation')
    QU_AUTOMATION_VALUE = 'yes'

    AUTOMATION_TOOLS = ('xpath', '//label[text()="Automation tools"]//following::ul/li')

    SUBMIT_BUTTON = ('xpath', '//button[@data-testid="submit-btn"]')
    
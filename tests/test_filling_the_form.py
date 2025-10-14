from data.urls import Urls
from pages.locators import MainPage
from data.data import Data
from pages import main_page


def test_fill_form(driver):

    page = main_page.MainPage(driver, Urls.BASE_URL)

    page.open()

    page.fill_in_input_field(MainPage.NAME_FIELD, Data.NAME)
    page.fill_in_input_field(MainPage.PASSWORD_FIELD, Data.PASSWORD)

    page.click(MainPage.FAV_DRINK_MILK)
    page.click(MainPage.FAV_DRINK_COFFEE)

    page.click(MainPage.FAV_COLOR)

    page.select(MainPage.QU_AUTOMATION, MainPage.QU_AUTOMATION_VALUE)

    page.fill_in_input_field(MainPage.EMAIL_FIELD, Data.EMAIL)

    text = (
        page.get_number_of_elements(MainPage.AUTOMATION_TOOLS)
        + " "
        + page.get_longest_element(MainPage.AUTOMATION_TOOLS)
    )
    page.fill_in_input_field(MainPage.MESSAGE_FIELD, text)

    page.scroll_to_and_click(MainPage.SUBMIT_BUTTON)

    assert page.get_alert_text() == Data.ALERT_MESSAGE

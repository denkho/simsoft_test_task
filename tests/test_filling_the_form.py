from pages.locators import MainPage
from data.data import Data
import allure


@allure.feature("Form submission")
@allure.story("Positive case: all fields filled correctly")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка успешной отправки формы при корректных данных")
def test_form_should_be_valid(open_main_page):
    page = open_main_page

    with allure.step("Заполняем поля формы корректными значениями"):
        page.fill_in_input_field(MainPage.NAME_FIELD, Data.NAME)
        page.fill_in_input_field(MainPage.PASSWORD_FIELD, Data.PASSWORD)

        page.click(MainPage.FAV_DRINK_MILK)
        page.click(MainPage.FAV_DRINK_COFFEE)

        page.click(MainPage.FAV_COLOR)

        page.select(MainPage.QU_AUTOMATION, MainPage.QU_AUTOMATION_VALUE)

        page.fill_in_input_field(MainPage.EMAIL_FIELD, Data.EMAIL)

    with allure.step(
        "Формируем текст сообщения из количества и длины элементов списка"
    ):
        text = (
            page.get_number_of_elements(MainPage.AUTOMATION_TOOLS)
            + " "
            + page.get_longest_element(MainPage.AUTOMATION_TOOLS)
        )
        page.fill_in_input_field(MainPage.MESSAGE_FIELD, text)

    with allure.step("Отправляем форму"):
        page.scroll_to_and_click(MainPage.SUBMIT_BUTTON)

    with allure.step("Проверяем сообщение об успешной отправке"):
        allert_text = page.get_alert_text()

        assert (
            allert_text == Data.ALERT_MESSAGE
        ), f"Alert message is {allert_text} and should be {Data.ALERT_MESSAGE}"


@allure.feature("Form submission")
@allure.story("Negative scenario: empty required field")
@allure.severity(allure.severity_level.NORMAL)
@allure.title(
    "Проверка невозможности отправки формы без заполнения обязательного поля Name"
)
def test_form_should_not_proceed_with_empy_required_field(open_main_page):
    page = open_main_page
    with allure.step("Не заполняем обязательное поле Name"):
        pass
    with allure.step("Пробуем отправить форму"):
        page.scroll_to_and_click(MainPage.SUBMIT_BUTTON)

    with allure.step("Проверяем, что алерт не появился"):
        assert (
            not page.is_alert_present()
        ), "Alert is present though form is not correct"

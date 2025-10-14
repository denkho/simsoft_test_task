from pages.base import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage(BasePage):
    def __init__(self, driver: WebDriver, url):
        super().__init__(driver, url)

    def get_number_of_elements(self, locator):
        return str(len(self.elements_are_visible(locator)))

    def get_longest_element(self, locator):
        elements = [x.text for x in self.elements_are_visible(locator)]
        max_len = max(len(s) for s in elements)
        return list(filter(lambda s: len(s) == max_len, elements))[0]
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser(request):
    print("\nStarting browser for tests...")

    options = Options()

    browser = webdriver.Chrome(options=options)
    yield browser

    print("\nQuiting browser...")
    browser.quit()

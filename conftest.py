import pytest
from selenium import webdriver


@pytest.fixture
def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    return options


@pytest.fixture
def driver(chrome_options):
    print("\nStarting browser for tests...")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    print("\nQuiting browser...")
    driver.quit()
